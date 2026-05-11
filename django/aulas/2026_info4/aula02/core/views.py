from django.shortcuts import render

def inicial(request):
    nome = 'BG'
    instituicao = 'IFRN'
    context = {
        'nome': nome,
        'instituto': instituicao
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def perfil(request):
    return render(request, 'perfil.html')

def cadastro_01(request):
    return render(request, 'cadastro_01.html')

def resposta_01(request):
    nome = request.POST['nome']
    cpf = request.POST['cpf']
    disciplina = request.POST['disc']
    context = {
        'nome': nome,
        'cpf': cpf,
        'disciplina': disciplina
    }
    return render(request, 'resposta_01.html', context)

def autenticacao(request):
    return render(request, 'login.html')

def autenticado(request):
    email = request.POST['email']
    senha = request.POST['senha']
    if email == 'admin@email.com' and senha == '123':
        return render(request, 'autenticado.html')
    else:
        return render(request, 'login.html')