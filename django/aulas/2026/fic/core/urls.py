from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('curso_galeria/', curso_galeria, name='curso_galeria'),

    path('area_listar', area_listar, name='area_listar'),
    path('area_cadastrar', area_cadastrar, name='area_cadastrar'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),
]