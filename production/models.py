from django.db import models
from django.db.models import F
from crops.models import CropVariety
from farm.models import Farm
from profiles.models import Farmer

class GrowthStage(models.Model):
    crop_variety = models.ForeignKey(CropVariety,related_name='stages', on_delete=models.SET_NULL,null=True)
    stage_number = models.IntegerField()
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    description = models.TextField()
    min_stage_duration = models.IntegerField(help_text="Days")
    max_stage_duration = models.IntegerField(help_text="Days")
    average_duration = models.IntegerField(editable=False)
    
    class Meta:
        unique_together = ['crop_variety', 'stage_number']
        ordering = ('crop_variety','stage_number')
        verbose_name = 'Growth Stage'
        verbose_name_plural = 'Growth Stages'
    def __str__(self):
        return f'{self.name}-{self.crop_variety}'
    
    def save(self, *args, **kwargs):
        # Calculate the average duration during save
        self.average_duration = (self.min_stage_duration + self.max_stage_duration) // 2
        super().save(*args, **kwargs)


class CropJourney(models.Model):
    crop_variety = models.ForeignKey(CropVariety,related_name='cropjournies', on_delete=models.SET_NULL,null=True)
    growth_stages = models.ManyToManyField(GrowthStage, through='CropJourneyStage')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    description = models.TextField()
    
    class Meta:
        ordering = ('crop_variety','name')
        verbose_name = 'Crop Journey'
        verbose_name_plural = 'Crop Journies'
        
    def __str__(self):
        return f'{self.name}-{self.crop_variety}'
    
    def journey_duration(self):
        total_duration = 0
        for journey_stage in self.cropjourneystage_set.all():
            total_duration += journey_stage.growth_stage.stage_duration
        return total_duration


class CropJourneyStage(models.Model):
    crop_journey = models.ForeignKey(CropJourney, on_delete=models.SET_NULL,null=True)
    growth_stage = models.ForeignKey(GrowthStage, on_delete=models.SET_NULL,null=True)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ['crop_journey', 'growth_stage']
        ordering = ['order']
        verbose_name = 'Crop Journey Stage'
        verbose_name_plural = 'Crop Journey Stages'
    
    def __str__(self):
        return f'{self.growth_stage.name}-{self.crop_journey.name}'


class FarmingJourney(models.Model):
    farmer = models.ForeignKey(Farmer,related_name='farmers',on_delete=models.DO_NOTHING)
    farm = models.ForeignKey(Farm,related_name='land',on_delete=models.DO_NOTHING)
    crop_journey= models.ForeignKey(CropJourney,related_name='farming',on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    completed= models.BooleanField(default=True)
    successful = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['crop_journey','farmer','farm','start_date']
        ordering = ['-timestamp']
        verbose_name = 'Farming Journey'
        verbose_name_plural = 'Farming Journies'
    
    def __str__(self):
        return f'{self.farmer.last_name}-{self.start_date}'
    