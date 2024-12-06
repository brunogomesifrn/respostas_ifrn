from django.shortcuts import render

def nome(request):
    
    context = {
        "meu_nome":"Bruno Gomes",
        "idade": 25,
        "curso": "TSI"
    }

    return render(request, 'nome.html', context)


def cadastro(request, nome, idade, curso):
    context = {
        "nome_url": nome,
        "idade": idade,
        "curso": curso,
    }
    return render(request, 'cadastro.html', context)

