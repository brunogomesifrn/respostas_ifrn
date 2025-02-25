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



def registro(request):
    '''
    form = UsuarioCriarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    '''
    if request.POST:

        usuario = {
        'nome': request.POST['nome'],
        'cpf': request.POST['cpf'],
        'telefone': request.POST['telefone'],
        'datanascimento': request.POST['datanascimento'],
        'email': request.POST['email'],
        'password': request.POST['password']
        }
        response = requests.post("http://localhost:3000/signup", data = json.dumps(usuario), headers={"Content-Type": "application/json"})
        if response.json()['msg'] == 'Usuário cadastrado com sucesso':
            return redirect('login')        
    
    return render(request, 'registro.html')




def autenticar(request):
    if request.POST:
        usuario = request.POST["usuario"]
        senha = request.POST["senha"]
        #user = authenticate(request, username=usuario, password=senha)

        autenticacao = {
            'email': usuario,
            'password': senha
        }

        resposta = requests.post('http://localhost:3000/signin', 
                data=json.dumps(autenticacao), 
                headers={"Content-Type": "application/json"})
        
        if('nome' in resposta.json()):
            '''
            se retornou usuário, deu certo a autenticação. 
            Então estou salvando na sessão o objeto json
            recebido.
            '''
            request.session['usuario'] = resposta.json()
            
            return redirect("perfil")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")




def perfil(request):
    '''
    Verifica se tem a chave 'usuario' na sessão. Se tiver, 
    é pq o usuário está autenticado e poderá abrir a página
    de Perfil. Caso não exista, não abrirá Perfil e redirecionará
    o usuário para login.
    '''
    if 'usuario' in request.session.keys():
        context = {
            'nome': request.session['usuario']['nome'],
            'email': request.session['usuario']['email']
        }   
        return render(request, 'perfil.html', context)
    else:
        return redirect('login')





def desconectar(request):
    #logout(request)
    '''
    Excluir a chave 'usuario' da sessão,
    desta forma o usuário estará deslogando.
    '''
    del request.session['usuario']
    return redirect("index")
