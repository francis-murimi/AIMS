from django.db import models
from django.db.models import F
from crops.models import CropVariety
from farm.models import Farm
from profiles.models import Farmer
from datetime import timedelta, date

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
            total_duration += journey_stage.growth_stage.average_duration
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
    completed= models.BooleanField(default=False)
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
    
    def get_current_growth_stage(self):
        start_date = self.start_date
        current_date = date.today()
        elapsed_days = (current_date - start_date).days

        # Calculate the total duration of growth stages in the crop journey
        total_duration = self.crop_journey.journey_duration()

        # Calculate the elapsed time as a percentage of the total duration
        progress_percentage = (elapsed_days / total_duration) * 100

        # Retrieve the crop journey stages ordered by the stage order
        crop_journey_stages = self.crop_journey.cropjourneystage_set.order_by('order')

        # Initialize variables to keep track of the current growth stage, remaining days/stages, and passed stages
        current_stage = None
        passed_stages = []
        accumulated_duration = 0
        remaining_days = 0
        remaining_stages = 0

        # Iterate over each growth stage to find the current stage
        for stage in crop_journey_stages:
            accumulated_duration += stage.growth_stage.average_duration
            if accumulated_duration >= progress_percentage:
                current_stage = stage.growth_stage
                remaining_days = total_duration - elapsed_days
                remaining_stages = crop_journey_stages.filter(order__gt=stage.order).count()
                break
            else:
                passed_stages.append(stage.growth_stage)
        passed_stages=len(passed_stages)
        return current_stage, progress_percentage, remaining_days, passed_stages, remaining_stages


    
    



    