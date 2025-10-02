from django import forms
from .models import Area

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']