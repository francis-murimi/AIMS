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