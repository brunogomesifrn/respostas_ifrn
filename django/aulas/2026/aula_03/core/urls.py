from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contato/', contato, name='contato'),
    path('cadastro_01/', cadastro_01, name='cadastro_01'),
    path('resposta_01/', resposta_01, name='resposta_01'),
]
