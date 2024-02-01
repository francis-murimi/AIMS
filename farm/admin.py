from django.contrib import admin

from farm.models import County, Village, Ward

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
    list_filter = ('ward__name','ward__code', 'ward__county__name',)
    search_fields = ('name','code','ward__name','ward__code','ward__county__name',)