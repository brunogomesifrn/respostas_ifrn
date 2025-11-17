from django import forms
from .models import Area, Publico, Instrutor

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']

class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome']