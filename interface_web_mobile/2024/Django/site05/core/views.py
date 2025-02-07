from django.shortcuts import render, redirect
from .models import Area, Publico, Curso
from .forms import AreaForm, PublicoForm, CursoForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AreaSerializer

@api_view(['GET'])
def areaAPIlistar(request):
    areas = Area.objects.all()
    areas_serializer = AreaSerializer(areas, many=True)
    return Response(areas_serializer.data)

@api_view(['PUT'])
def areaAPIadicionar(request):
    area = AreaSerializer(data=request.data)
    if area.is_valid():
        area.save()
        return Response(area.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def areaAPIatualizar(request, id):
    area_bd = Area.objects.get(id=id)
    area = AreaSerializer(data=request.data,
                                 instance=area_bd)
    if area.is_valid():
        area.save()
        return Response(area.data, status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def areaAPIremover(request, id):
    area_bd = Area.objects.get(id=id)
    if area_bd:
        area_bd.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

def index(request):
    return render(request, 'index.html')

'''

============= ÁREAS =============

'''

def areas(request):
    areas = Area.objects.all()
    contexto = {
        'areas': areas
    }
    return render(request, 'areas.html', contexto)

def area_cadastrar(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('areas')
    contexto = {
        'form': form
    }
    return render(request, 'area_cadastrar.html', contexto)


def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('areas')
    contexto = {
        'form': form
    }
    return render(request, 'area_cadastrar.html', contexto)


def area_remover(request, id):
    area =  Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')


'''

============= PÚBLICOS =============

'''

def publicos(request):
    publicos = Publico.objects.all()
    contexto = {
        'publicos': publicos
    }
    return render(request, 'publicos.html', contexto)

def publico_cadastrar(request):
    form = PublicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form': form
    }
    return render(request, 'publico_cadastrar.html', contexto)


def publico_editar(request, id):
    publico = Publico.objects.get(pk=id)
    form = PublicoForm(request.POST or None, instance=publico)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form': form
    }
    return render(request, 'publico_cadastrar.html', contexto)


def publico_remover(request, id):
    publico =  Publico.objects.get(pk=id)
    publico.delete()
    return redirect('publicos')




'''

============= CURSOS =============

'''

def cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        'cursos': cursos
    }
    return render(request, 'cursos.html', contexto)

def curso_cadastrar(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastrar.html', contexto)


def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastrar.html', contexto)


def curso_remover(request, id):
    curso =  Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

