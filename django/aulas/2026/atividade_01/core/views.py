from django.shortcuts import render

def inicial(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def sucesso(request):
    if request.POST:
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        nascimento = request.POST['nascimento']
        ocupacoes = request.POST.getlist('ocupacao[]')

        context = {
            'nome': nome,
            'cpf': cpf,
            'nascimento': nascimento,
            'ocupacoes': ocupacoes,

        }
        return render(request, 'sucesso.html', context)
    return render(request, 'cadastro.html')

def autenticacao(request):
    return render(request, 'autenticacao.html')

def perfil(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        if usuario=='admin@email.com' and senha=='123':
            return render(request, 'perfil.html')
        else:
            return render(request, 'autenticacao.html')
        
    else:
        return render(request, 'autenticacao.html')