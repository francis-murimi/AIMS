from django.contrib import admin

from farm.models import County, Village, Ward

# Register your models here.
@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('name', 'county',)
    list_filter = ('county__name',)
    search_fields = ('name', 'county__name',)

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('name', 'ward',)
    list_filter = ('ward__name', 'ward__county__name',)
    search_fields = ('name', 'ward__name', 'ward__county__name',)