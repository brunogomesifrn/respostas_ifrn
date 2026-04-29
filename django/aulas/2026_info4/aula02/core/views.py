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
    context = {
        'nome': nome
    }
    return render(request, 'resposta_01.html', context)