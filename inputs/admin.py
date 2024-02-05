from django.contrib import admin
from inputs.models import Input, InputCategory


@admin.register(InputCategory)
class InputCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','code',)
    search_fields = ('name','code','description',)
    

@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display = ('name','code',)
    list_filter = ('input_category__name',)
    search_fields = ('name','code','description','input_category__name','input_category__code')