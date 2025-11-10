from django.shortcuts import render, redirect
from .models import Area, Publico, Instrutor, Curso
from .forms import AreaForms, PublicoForms, InstrutorForms, CursoForms


def areas(request):
    areas = Area.objects.all()
    context = {
        'areas':areas
    }
    return render(request, 'areas.html', context)

def area_cadastro(request):
    form = AreaForms(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('areas')

    context = {
        'form': form
    }
    return render(request, 
        'area_cadastro.html', context)


def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')

def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForms(request.POST or None,
                     instance=area)
    if form.is_valid():
        form.save()
        return redirect('areas')

    context = {
        'form':form
    }
    return render(request, 
        'area_cadastro.html', context)


# ===================================


def publicos(request):
    publicos = Publico.objects.all()
    context = {
        'publicos':publicos
    }
    return render(request, 'publicos.html', context)

def publico_cadastro(request):
    form = PublicoForms(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('publicos')

    context = {
        'form': form
    }
    return render(request, 'publico_cadastro.html', context)

def publico_remover(request, id):
    publico = Publico.objects.get(pk=id)
    publico.delete()
    return redirect('publicos')

def publico_editar(request, id):
    publico = Publico.objects.get(pk=id)
    form = PublicoForms(request.POST or None, instance=publico)
    if form.is_valid():
        form.save()
        return redirect('publicos')

    context = {
        'form':form
    }
    return render(request, 'publico_cadastro.html', context)

# ===================================


def instrutores(request):
    instrutores = Instrutor.objects.all()
    context = {
        'instrutores':instrutores
    }
    return render(request, 'instrutores.html', context)

def instrutor_cadastro(request):
    form = InstrutorForms(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('instrutores')

    context = {
        'form': form
    }
    return render(request, 'instrutor_cadastro.html', context)

def instrutor_remover(request, id):
    instrutor = Instrutor.objects.get(pk=id)
    instrutor.delete()
    return redirect('instrutores')

def instrutor_editar(request, id):
    instrutor = Instrutor.objects.get(pk=id)
    form = InstrutorForms(request.POST or None, instance=instrutor)
    if form.is_valid():
        form.save()
        return redirect('instrutores')

    context = {
        'form':form
    }
    return render(request, 'instrutor_cadastro.html', context)


# =============================

def cursos(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos.html', context)

def curso_cadastro(request):
    form = CursoForms(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('cursos')

    context = {
        'form':form
    }

    return render(request, 'curso_cadastrar.html', context)

def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForms(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    context = {
        'form':form
    }
    return render(request, 'curso_cadastrar.html', context)


