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