from django.db import models

class Area(models.Model):
    nome = models.CharField("Nome", max_length=50)
    def __str__(self):
        return self.nome

class PublicoAlvo(models.Model):
    nome = models.CharField("Nome", max_length=50)

class Curso(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    ch = models.IntegerField("Carga-horária")
    data = models.DateTimeField("Data e hora de início")
    vagas = models.IntegerField("Vagas")
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(PublicoAlvo)
