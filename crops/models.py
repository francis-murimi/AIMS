from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=15,unique=True,db_index=True)
    description = models.TextField(max_length=500)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Crop'
        verbose_name_plural = 'Crops'
    def __str__(self):
        return f'{self.name}'

class FoodGroup(models.Model):
    name = models.CharField(max_length=20,unique=True,db_index=True)
    description = models.TextField(max_length=500)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Food Group'
        verbose_name_plural = 'Food Groups'
    def __str__(self):
        return f'{self.name}'

class CropVariety(models.Model):
    name = models.CharField(max_length=30,unique=True,db_index=True)
    crop = models.ForeignKey(Crop,on_delete=models.SET_NULL,null=True)
    food_group = models.ForeignKey(FoodGroup,on_delete=models.SET_NULL,null=True)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Crop Variety'
        verbose_name_plural = 'Crop Varieties'
    def __str__(self):
        return f'{self.name}-{self.crop}'
    