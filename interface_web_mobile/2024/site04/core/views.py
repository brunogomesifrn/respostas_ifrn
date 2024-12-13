from django.shortcuts import render
from .models import Area

def areas(request):
    areas = Area.objects.all()
    context = {
        'areas': areas
    }

    return render(request, 'areas.html', context)

def area_cadastro(request):
    return render(request, 'area_cadastro.html')