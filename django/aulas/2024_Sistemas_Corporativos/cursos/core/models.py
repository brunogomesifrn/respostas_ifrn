from django.db import models

class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=50)
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    cpf = models.CharField('CPF', max_length=11, primary_key=True)
    nome = models.CharField('Nome', max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    def __str__(self):
        return (self.cpf+' - '+self.nome)

class Projeto(models.Model):
    codigo = models.IntegerField('Código', primary_key=True)
    titulo = models.CharField('Título', max_length=200)
    valor = models.DecimalField('Valor', max_digits=9, decimal_places=2)
    inicio = models.DateField('Início')
    funcionarios = models.ManyToManyField(Funcionario)
    def __str__(self):
        return self.titulo

