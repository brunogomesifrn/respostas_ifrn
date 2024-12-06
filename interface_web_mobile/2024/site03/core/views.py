from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def cadastro_resultado(request):
    nome = request.POST['nome']
    cpf = request.POST['cpf']

    context = {
        'nome_digitado': nome,
        'cpf_digitado': cpf
    }

    return render(request, 'cadastro_resultado.html', context)