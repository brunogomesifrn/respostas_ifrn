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

def cadastro_01(request):
    return render(request, 'cadastro_01.html')

def resposta_01(request):
    if request.POST:
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        disciplina = request.POST['disc']
        context = {
            'nome': nome,
            'cpf': cpf,
            'disciplina': disciplina
        }
        return render(request, 'resposta_01.html', context)
    return render(request, 'cadastro_01.html')