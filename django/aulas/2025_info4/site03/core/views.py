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
    linguagem = request.POST['linguagem']
    
    contexto = {
        'nome_digitado': nome,
        'cpf': cpf,
        'linguagem': linguagem
        }

    return render(request, 'resultado.html', contexto)
