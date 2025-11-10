from django.urls import path
from .views import areas, area_cadastro, area_remover, area_editar
from .views import publicos, publico_cadastro, publico_remover, publico_editar
from .views import instrutores, instrutor_cadastro, instrutor_remover, instrutor_editar
from .views import cursos, curso_cadastro, curso_remover, curso_editar

urlpatterns = [
     path('areas/', areas, name='areas'),
     path('area_cadastro/',area_cadastro, name='area_cadastro'),
     path('area_remover/<int:id>/', area_remover, name='area_remover'),
     path('area_editar/<int:id>/', area_editar, name='area_editar'),

     path('publicos/', publicos, name='publicos'),
     path('publico_cadastro/',publico_cadastro, name='publico_cadastro'),
     path('publico_remover/<int:id>/', publico_remover, name='publico_remover'),
     path('publico_editar/<int:id>/', publico_editar, name='publico_editar'),

     path('instrutores/', instrutores, name='instrutores'),
     path('instrutor_cadastro/',instrutor_cadastro, name='instrutor_cadastro'),
     path('instrutor_remover/<int:id>/', instrutor_remover, name='instrutor_remover'),
     path('instrutor_editar/<int:id>/', instrutor_editar, name='instrutor_editar'),

     path('cursos/', cursos, name='cursos'),
     path('curso_cadastro', curso_cadastro, name='curso_cadastro'),
     path('curso_remover/<int:id>/', 
          curso_remover, name='curso_remover'),
     path('curso_editar/<int:id>/', curso_editar, 
          name='curso_editar')
]

