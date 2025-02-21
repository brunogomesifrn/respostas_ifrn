from django.shortcuts import render, redirect
from .forms import UsuarioCriarForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User

import requests
import json
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def perfil(request):
    
context = {

'nome': request.SESSION['nome']
'email': request.SESSION['email']
}
    return render(request, 'perfil.html')

def registro(request):
    form = UsuarioCriarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    context = {
        'form': form
    }
    return redirect('login')
    return render(request, 'registro.html', context)

def autenticar(request):
    if request.POST:
        usuario = request.POST["usuario"]
        senha = request.POST["senha"]
        #user = authenticate(request, username=usuario, password=senha)
        autenticacao = {
            'email': usuario,
            'password': senha
        }

        resposta = requests.post('http://10.41.1.179:3000/signin', 
                data=json.dumps(autenticacao), 
                headers={"Content-Type": "application/json"})
        
        if('nome' in resposta.json()):
            request.SESSION['nome'] = resposta.json()['nome']
            request.SESSION['email'] = resposta.json()['email']
            
            return redirect("perfil")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")

def desconectar(request):
    logout(request)
    return redirect("index")
