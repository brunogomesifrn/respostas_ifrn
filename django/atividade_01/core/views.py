from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def nome(request):
    return render(request, "nome.html")

def campus(request):
    return render(request, "campus.html")