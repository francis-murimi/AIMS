from django.db import models

# Create your models here.
class County(models.Model):  
    name = models.CharField(max_length=10,db_index=True)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    class Meta:
        ordering = ('name',)
        verbose_name = 'County'
        verbose_name_plural = 'Counties'
    def __str__(self):
        return f'{self.name}'
     

class Ward(models.Model): 
    name = models.CharField(max_length=15)
    county = models.ForeignKey(County,on_delete=models.SET_NULL,null=True)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Ward'
        verbose_name_plural = 'Wards'
    def __str__(self):
        return f'{self.name}--{self.county}'

class Village(models.Model):
    name = models.CharField(max_length=20)
    ward = models.ForeignKey(Ward,on_delete=models.SET_NULL,null=True)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Village'
        verbose_name_plural = 'Villages'
    
    def __str__(self):
        return f'{self.name}--{self.ward}'
    

class Soil(models.Model):
    TEXTURE_CHOICES = [
        ('sandy', 'sandy'),
        ('clay', 'clay'),
        ('silty', 'silty'),
        ('loamy', 'loamy'),
    ]
    COLOR_CHOICES = [
        ('brown', 'brown'),
        ('black', 'black'),
        ('red', 'red'),
        ('yellow', 'yellow'),
    ]
    ACIDITY_CHOICES = [
        ('acidic', 'acidic'),
        ('neutral', 'neutral'),
        ('alkaline', 'alkaline'),
    ]
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    texture = models.CharField(max_length=20, choices=TEXTURE_CHOICES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    depth = models.IntegerField()
    structure = models.CharField(max_length=50)
    porosity = models.FloatField()
    stone_content = models.FloatField()
    acidity_level = models.CharField(max_length=20, choices=ACIDITY_CHOICES)
    description = models.TextField(max_length=500)
    
    class Meta:
        ordering = ('code',)
        verbose_name = 'Soil'
        verbose_name_plural = 'Soils'
        
    def __str__(self):
        return f"{self.color}-{self.acidity_level}-{self.texture}"


class WaterSource(models.Model):
    WATER_TYPE_CHOICES = [
        ('acidic', 'acidic'),
        ('salty', 'salty'),
        ('fresh', 'fresh'),
    ]

    TYPE_CHOICES = [
        ('dam', 'dam'),
        ('river', 'river'),
        ('well', 'well'),
        ('rain', 'rain'),
        ('other', 'other'),
    ]

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    water_type = models.CharField(max_length=20, choices=WATER_TYPE_CHOICES)
    water_source_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_seasonal = models.BooleanField(default=False)
    water_capacity = models.DecimalField(help_text='Meters cubed',decimal_places=2,max_digits=10)
    is_shared = models.BooleanField(default=True)
    is_dry = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Water Source'
        verbose_name_plural = 'Water Sources'

    def __str__(self):
        return f"{self.name}-{self.water_source_type}"


class Farm(models.Model):
    SLOPE_CHOICES = [
        ('flat', 'flat'),
        ('east', 'east'),
        ('west', 'west'),
        ('north', 'north'),
        ('south', 'south'),
    ]
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    location = models.ForeignKey(Village,on_delete=models.SET_NULL,null=True)
    size = models.DecimalField(help_text='Acres',decimal_places=2,max_digits=7)
    water_source = models.ForeignKey(WaterSource,on_delete=models.SET_NULL,null=True)
    soil = models.ForeignKey(Soil,on_delete=models.SET_NULL,null=True)
    slope = models.CharField(max_length=20, choices=SLOPE_CHOICES)
    
    class Meta:
        ordering = ('code',)
        verbose_name = 'Farm'
        verbose_name_plural = 'Farms'

    def __str__(self):
        return f"{self.code}-{self.location}"

