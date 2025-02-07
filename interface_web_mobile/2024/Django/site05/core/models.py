from django.db import models

class Area(models.Model):
    nome = models.CharField('Area', max_length=100)
    def __str__(self):
        return self.nome


class Publico(models.Model):
    nome = models.CharField('Publico', max_length=100)
    def __str__(self):
        return self.nome


class Curso(models.Model):
    titulo = models.CharField('Titulo', max_length=300)
    descricao = models.TextField('Descricao')
    autor = models.CharField('Autor(es)', max_length=200)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)
    def __str__(self):
        return self.titulo