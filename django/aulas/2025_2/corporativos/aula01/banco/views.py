from django.shortcuts import render
from .models import Area


def areas(request):
    areas = Area.objects.all()
    context = {
        'areas':areas
    }
    return render(request, 'areas.html', context)
