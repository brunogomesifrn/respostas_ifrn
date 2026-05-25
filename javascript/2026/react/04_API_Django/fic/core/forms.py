from django import forms
from .models import Area, PublicoAlvo

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoAlvo(forms.ModelForm):
    class Meta:
        model = PublicoAlvo
        fields = ['nome']