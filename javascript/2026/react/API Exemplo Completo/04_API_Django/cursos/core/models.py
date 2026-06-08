from django.db import models

class Areas(models.Model):
    nome = models.CharField("Nome", max_length=100)

class Publicos(models.Model):
	nome = models.CharField('Nome', max_length=100)

class Cursos(models.Model):
	titulo = models.CharField('Nome', max_length=150)
	resumo = models.TextField('Resumo', max_length=500)
	carga_horaria = models.IntegerField('Carga Horária')
	data_inicio = models.DateField('Data de Início')
	vagas = models.IntegerField('Vagas')
	area = models.ForeignKey(Areas, on_delete=models.PROTECT)
	publicos = models.ManyToManyField(Publicos)
	foto = models.ImageField('Foto', upload_to='media', blank=True, null=True)
