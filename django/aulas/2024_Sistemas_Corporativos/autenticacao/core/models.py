from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nome = models.CharField('Nome', max_length=500)
    cpf = models.CharField('CPF', max_length=11)

    USERNAME_FIELD = 'username'

