from django.shortcuts import render, redirect
from .models import Area
from .forms import AreaForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def curso_galeria(request):
    return render(request, 'curso_galeria.html')

def area_listar(request):
    areas = Area.objects.all()
    context = {
        'areas': areas
    }
    #return render(request, 'areas.html', context)
    return render(request, 'privado/areas.html', context)

def area_cadastrar(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('area_listar')
    context = {
        'form': form
    }
    #return render(request, 'area_cadastrar.html', context)
    return render(request, 'privado/area_cadastrar.html', context)

def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('area_listar')
    context = {
        'form': form
    }
    #return render(request, 'area_cadastrar.html', context)
    return render(request, 'privado/area_cadastrar.html', context)

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('area_listar')