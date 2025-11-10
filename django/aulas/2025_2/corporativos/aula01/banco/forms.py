from django import forms
from .models import Area, Publico, Instrutor, Curso

class AreaForms(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoForms(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']

class InstrutorForms(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome']

class CursoForms(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descricao', 'vagas', 
                  'instrutor', 'area',
                    'publicos']
        widgets = {
            'area': forms.RadioSelect(),
            'publicos': forms.CheckboxSelectMultiple(),
            'instrutor': forms.RadioSelect()
        }
    