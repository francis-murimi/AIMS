from django.contrib import admin

from farm.models import County, Farm, Soil, Village, Ward, WaterSource

# Register your models here.
@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name','code',)
    search_fields = ('name','code',)

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('name','code','county',)
    list_filter = ('county__name',)
    search_fields = ('name','code','county__name',)

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('name','code','ward',)
    list_filter = ('ward__name', 'ward__county__name',)
    search_fields = ('name','code','ward__name','ward__code','ward__county__name',)

@admin.register(Soil)
class SoilAdmin(admin.ModelAdmin):
    list_display = ('code', 'texture', 'color', 'depth', 'structure', 'porosity', 'stone_content', 'acidity_level')
    search_fields = ('code', 'texture', 'color', 'structure', 'acidity_level')

@admin.register(WaterSource)
class WaterSourceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'water_type', 'water_source_type', 'is_seasonal', 'water_capacity', 'is_shared', 'is_dry')
    search_fields = ('code', 'name', 'water_type', 'water_source_type')
    list_filter = ('location__ward__name','location__ward__county__name',)

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('code', 'location', 'size', 'water_source', 'soil', 'slope')
    search_fields = ('code', 'location__name', 'water_source__name', 'soil__code', 'slope')
    list_filter = ('slope','location__ward__name', 'location__ward__county__name',)

    def location(self, obj):
        return obj.location.name if obj.location else None
    location.short_description = 'Location'