from rest_framework import serializers
from .models import Areas

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ['id', 'nome']