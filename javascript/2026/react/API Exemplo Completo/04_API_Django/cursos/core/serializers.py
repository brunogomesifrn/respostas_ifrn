from rest_framework import serializers
from .models import Areas, Publicos, Cursos

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ['id', 'nome']

class PublicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicos
        fields = ['id', 'nome']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = [
            'id',
            'titulo',
            'resumo',
            'carga_horaria',
            'data_inicio',
            'vagas',
            'area',
            'publicos'
        ]