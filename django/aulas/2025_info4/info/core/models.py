from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11)
    nome_completo = models.CharField('Nome Completo', max_length=50)

    

class Area(models.Model):
    nome = models.CharField('Nome', max_length=50)

class Instrutor(models.Model):
    nome = models.CharField('Instrutor', max_length=50)

class Publico(models.Model):
    nome = models.CharField('Público', max_length=50)

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição')
    vagas = models.IntegerField('Vagas')
    instrutor = models.ForeignKey(Instrutor, 
                                  on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)







class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=50)

class Projeto(models.Model):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição')
    categoria = models.ForeignKey(Categoria, 
                    on_delete=models.PROTECT)

class Aluno(models.Model):
    matricula = models.CharField('Matrícula', 
                max_length=14, primary_key=True)
    nome = models.TextField('Nome')
    email = models.TextField('E-mail')
    projeto = models.ForeignKey(Projeto, 
                                on_delete=models.PROTECT)
