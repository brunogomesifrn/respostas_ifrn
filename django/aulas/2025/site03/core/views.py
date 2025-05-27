from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def resultado(request):
    nome = request.POST['nome']
    cpf = request.POST['cpf']

    contexto = {
        'nome_digitado':nome,
        'cpf': cpf
        }

    return render(request, 'resultado.html', contexto)
