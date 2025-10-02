from django.shortcuts import render
from .models import Area

def index(request):
    return render(request, 'index.html')

def categorias(request):
    return render(request, 'categorias.html')

def areas(request):
    areas = Area.objects.all()
    
    return render(request, 'areas.html')