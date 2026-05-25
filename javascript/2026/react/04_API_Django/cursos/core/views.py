from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Areas
from .serializers import AreasSerializer
from rest_framework.response import Response

@api_view(['GET'])
def AreasListarAPI(request):
    lista_areas = Areas.objects.all()
    serializer = AreasSerializer(lista_areas, many=True)
    return Response(serializer.data)

