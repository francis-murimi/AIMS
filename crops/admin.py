from django.contrib import admin
from crops.models import Crop, CropVariety, FoodGroup

# Register your models here.
@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name','code',)
    search_fields = ('name','code',)

@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    list_display = ('name','code',)
    search_fields = ('name','code','description',)

@admin.register(CropVariety)
class CropVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','code','crop','food_group',)
    list_filter = ('crop__name','food_group__name',)
    search_fields = ('name','code','crop__name','crop__code','food_group__name','food_group__code',)