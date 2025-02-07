from django import forms
from .models import Area

class AreaForms(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']
