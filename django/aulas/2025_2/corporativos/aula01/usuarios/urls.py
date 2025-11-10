from django.urls import path
from .views import autenticacao, perfil, desconectar

urlpatterns = [
    path('autenticacao/', autenticacao, name='autenticacao'),
    path('desconectar/', desconectar, name='desconectar'),
    path('perfil/', perfil, name='perfil'),
    
]

