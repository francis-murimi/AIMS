from django.contrib import admin
from .models import Farmer

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','middle_name','last_name', 'gender','phone_number')
    list_filter = ('gender', 'timestamp', 'date_updated','date_of_birth')
    search_fields = ('first_name','first_name','last_name', 'phone_number')