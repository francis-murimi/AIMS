from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Farmer(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10,null=True,blank=True,validators=[
            RegexValidator(
                regex='^\d+$'
            )
        ])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12, validators=[
            RegexValidator(
                regex=r'^(\+?254|0)?\d{9}$',
                message="Phone number must start with '254' and contain 12 digits (including country code) or 10 digits (without country code)."
            )
        ])
    date_of_birth = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('timestamp',)
        verbose_name = 'Farmer'
        verbose_name_plural = 'Farmers'

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
        
    
