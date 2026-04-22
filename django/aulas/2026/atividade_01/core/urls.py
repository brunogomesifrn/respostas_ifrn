from django.urls import path
from .views import *

urlpatterns = [
    path('', inicial, name='inicial'),
    path('cadastro/', cadastro, name='cadastro'),
    path('sucesso/', sucesso, name='sucesso'),
    path('autenticacao/', autenticacao, name='autenticacao'),
    path('perfil/', perfil, name='perfil'),
]