from django.db import models

class Areas(models.Model):
    nome = models.CharField("Nome", max_length=100)
