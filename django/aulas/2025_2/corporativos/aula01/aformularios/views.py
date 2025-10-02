from django.shortcuts import render

def cadastro(request):
    return render(request, 'cadastro.html')

def dados(request):
    nome = request.POST['nome']
    cpf = request.POST['cpf']
    disciplina = request.POST['disc']

    context = {
        'nome':nome,
        'cpf':cpf,
        'disciplina': disciplina
    }

    return render(request, 'dados.html', context)