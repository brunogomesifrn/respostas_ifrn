from django.shortcuts import render

def inicial(request):
    return render(request, 'index.html')

