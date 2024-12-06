from django.db import models

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Publico(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=200)
    descricao = models.TextField('Descrição')
    autor = models.CharField('Autor', max_length=100)
    vagas = models.IntegerField('Vagas')
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)

    
