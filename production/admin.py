from django.contrib import admin
from production.models import CropJourney, CropJourneyStage, FarmingJourney, GrowthStage


@admin.register(GrowthStage)
class GrowthStageAdmin(admin.ModelAdmin):
    list_display = ('name','code','crop_variety','stage_number',)
    list_filter = ('crop_variety','stage_number',)
    search_fields = ('name','code','crop_variety__name','stage_number','description')


@admin.register(CropJourney)
class CropJourneyAdmin(admin.ModelAdmin):
    list_display = ('name','code','crop_variety',)
    list_filter = ('crop_variety',)
    search_fields = ('name','code','crop_variety__name','crop_variety__crop__name','description')


@admin.register(CropJourneyStage)
class CropJourneyStageAdmin(admin.ModelAdmin):
    list_display = ('crop_journey',)
    search_fields = ('crop_journey__crop_variety__crop__name','crop_journey__crop_variety__crop__name')

@admin.register(FarmingJourney)
class FarmingJourneyAdmin(admin.ModelAdmin):
    list_display = ('farm','farmer','crop_journey','completed','start_date',)
    list_filter = ('farm__location__ward__name','crop_journey__crop_variety__crop__name','start_date','completed','successful')
    search_fields = ('farm__location__ward__name','crop_journey__crop_variety__crop__name','farmer__id_number','farmer__phone_number')
    