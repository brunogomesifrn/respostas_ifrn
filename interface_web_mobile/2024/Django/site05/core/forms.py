from django import forms
from .models import Area, Publico, Curso

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descricao', 'autor', 'area', 'publicos']
        widgets = {
            'area': forms.RadioSelect(),
            'publicos': forms.CheckboxSelectMultiple(),
        }
