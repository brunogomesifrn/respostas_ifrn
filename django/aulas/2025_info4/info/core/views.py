from django.shortcuts import render, redirect
from .models import Area, Publico, Instrutor
from .forms import AreaForm, PublicoForm, InstrutorForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticacao(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, 
                            username=usuario,
                            password=senha)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def desconectar(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def categorias(request):
    return render(request, 'categorias.html')

def areas(request):
    areas = Area.objects.all()
    contexto = {
        'lista_areas': areas
    }
    return render(request, 'areas.html', contexto)

def area_cadastro(request):
    form = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('areas')

    contexto = {
        'form':form
    }
    return render(request, 'area_cadastro.html', contexto)

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')

def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)

    if form.is_valid():
        form.save()
        return redirect('areas')
    
    contexto = {
        'form':form
    }

    return render(request, 'area_cadastro.html', contexto)




def publicos(request):
    publicos = Publico.objects.all()
    contexto = {
        'publicos': publicos
    }
    return render(request, 'publicos.html', contexto)

def publico_cadastrar(request):
    form = PublicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form':form
    }
    return render(request, 'publico_cadastrar.html', contexto)

def publico_remover(request,id):
    publico = Publico.objects.get(pk=id)
    publico.delete()
    return redirect('publicos')

def publico_editar(request, id):
    publico = Publico.objects.get(pk=id)
    form = PublicoForm(request.POST or None, instance=publico)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form':form
    }
    return render(request, 'publico_cadastrar.html', contexto)