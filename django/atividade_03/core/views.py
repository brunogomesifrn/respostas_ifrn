from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def pagina2(request):
    return render(request, "pagina_2.html")

def pagina3(request):
    return render(request, "pagina_3.html")