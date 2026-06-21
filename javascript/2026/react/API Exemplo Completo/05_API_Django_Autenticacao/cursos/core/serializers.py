from rest_framework import serializers
from .models import Areas, Publicos, Cursos
from core.models import Usuario

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UsuarioCadastroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    class Meta:
        model = Usuario
        fields = [
            'username',
            'password',
            'nome_completo',
            'email',
            'cpf',
            'matricula'
        ]

    def create(self, validated_data):
        senha = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(senha)
        usuario.save()
        return usuario


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