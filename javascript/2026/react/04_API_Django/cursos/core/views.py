from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Areas
from .serializers import AreasSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def AreasListarAPI(request):
    lista_areas = Areas.objects.all()
    serializer = AreasSerializer(lista_areas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def AreaInserirAPI(request):
    serializer = AreasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def AreaEditarAPI(request, id):
    #area = Areas.objects.get(pk=id)
    area = get_object_or_404(Areas, pk=id)
    serializer = AreasSerializer(data=request.data, instance=area)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)
    return Response(serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST)