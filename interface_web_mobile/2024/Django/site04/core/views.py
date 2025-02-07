from django.shortcuts import render, redirect
from .models import Area
from .forms import AreaForms

def areas(request):
    areas = Area.objects.all()
    context = {
        'areas': areas
    }

    return render(request, 'areas.html', context)

def area_cadastro(request):
    form = AreaForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('areas')
    context = {
        'form': form
    }
    return render(request, 'area_cadastro.html', context)

def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForms(request.POST or None, instance=area)
    if form.is_valid():
        form.save()
        return redirect('areas')
    context = {
        'form': form
    }
    return render(request, 'area_cadastro.html', context)

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')