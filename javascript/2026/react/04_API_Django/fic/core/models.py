from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11, primary_key=True)
    email = models.CharField('E-mail', max_length=200, unique=True)
    nascimento = models.DateField('Data de Nascimento')
    def __str__(self):
        return self.cpf

class Area(models.Model):
    nome = models.CharField("Nome", max_length=50)
    def __str__(self):
        return self.nome

class PublicoAlvo(models.Model):
    nome = models.CharField("Nome", max_length=50)
    def __str__(self):
        return self.nome    

class Curso(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    ch = models.IntegerField("Carga-horária")
    data = models.DateField("Data de início", null=True, blank=True)
    vagas = models.IntegerField("Vagas")
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(PublicoAlvo)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    def __str__(self):
        return self.titulo
