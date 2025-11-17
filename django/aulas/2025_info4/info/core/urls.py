from django.urls import path
from .views import index, categorias
from .views import areas, area_cadastro, area_remover, area_editar
from .views import publicos, publico_cadastrar, publico_editar, publico_remover
from .views import perfil, autenticacao, desconectar

urlpatterns = [

    path('perfil/', perfil, name='perfil'),
    path('login/', autenticacao, name='login'),
    path('desconectar/', desconectar, name='desconectar'),

    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),

    path('areas/', areas, name='areas'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),
    path('area_editar/<int:id>/', area_editar,name='area_editar'),

    path('publicos/', publicos, name='publicos'),
    path('publico_cadastrar', publico_cadastrar, name='publico_cadastrar'),
    path('publico_remover/<int:id>/', publico_remover, name='publico_remover'),
    path('publico_editar/<int:id>', publico_editar, name='publico_editar'),
]
