from django.shortcuts import render

def nome(request, nome):
    contexto = {
        'nome': nome
    }
    return render(request, 'nome.html', contexto)


def idade(request, idade):
    ano = 2022-idade
    contexto = {
        'idade': idade,
        'ano': ano,
    }
    return render(request, 'idade.html', contexto)

def media(request, nota1, nota2):
    media = (float(nota1) + float(nota2))/2

    contexto = {
        'media': media,
    }
    return render(request, 'media.html', contexto)
