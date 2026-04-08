from django.shortcuts import render

def inicio(request):
    nome = 'BG'
    context = {
        'identificador': nome,
        'instituicao': 'IFRN'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')