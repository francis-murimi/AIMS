from django.db import models

# Create your models here.
class InputCategory(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    description = models.TextField(max_length=500)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Input Category'
        verbose_name_plural = 'Input Categories'
    def __str__(self):
        return f'{self.name}'

class Input(models.Model):
    MEASURING_UNITS = [
        ('litres', 'litres'),
        ('kilograms', 'kilograms'),
        ('50kg bags', '50kg bags'),
        ('tonnes', 'tonnes'),
    ]
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=15,unique=True,db_index=True,blank=False,null=False)
    input_category = models.ForeignKey(InputCategory,on_delete=models.SET_NULL,null=True,blank=True)
    description = models.TextField(max_length=500)
    measuring_unit = models.CharField(max_length=20,choices=MEASURING_UNITS)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Input'
        verbose_name_plural = 'Inputs'
    def __str__(self):
        return f'{self.name}'