from django.shortcuts import render

def inicial(request):
    return render(request, 'index.html')

def curso_galeria(request):
    return render(request, 'curso_galeria.html')