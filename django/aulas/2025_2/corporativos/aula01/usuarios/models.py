from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cpf = models.CharField('CPF', max_length=11)
    nome_completo = models.CharField('Nome Completo', max_length=100)

    USERNAME_FIELD = 'username'