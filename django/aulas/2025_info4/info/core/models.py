from django.db import models

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
