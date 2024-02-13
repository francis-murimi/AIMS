from django import forms
from .models import FarmingJourney

class FarmingJourneyForm(forms.ModelForm):
    class Meta:
        model = FarmingJourney
        fields = ['farmer','farm','crop_journey','start_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
