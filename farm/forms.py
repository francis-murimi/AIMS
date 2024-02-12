from django import forms
from .models import Farm

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['code', 'location', 'size', 'water_source', 'soil', 'slope']
