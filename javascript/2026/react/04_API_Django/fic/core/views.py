from django.shortcuts import render
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
    return render(request, 'areas.html', context)
