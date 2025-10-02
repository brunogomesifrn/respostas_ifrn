from django.db import models

# Create your models here.
class Area(models.Model):
    nome = models.CharField('Nome', max_length=50)

class Publico(models.Model):
    nome = models.CharField('Público', max_length=50)

class Instrutor(models.Model):
    nome = models.CharField('Instrutor', max_length=50)

class Curso(models.Model):
    titulo = models.CharField('Curso', max_length=100)
    descricao =  models.TextField('Descrição', null=True)
    vagas = models.IntegerField('Vagas')
    instrutor = models.ForeignKey(Instrutor, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)