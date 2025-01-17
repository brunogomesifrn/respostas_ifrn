from django.urls import path
from .views import index
from .views import areas, area_cadastrar, area_editar, area_remover
from .views import publicos, publico_cadastrar, publico_editar, publico_remover
from .views import cursos, curso_cadastrar, curso_editar, curso_remover

urlpatterns = [

    path('', index, name='index'),

    # ==== ÁREA ====
    path('areas/', areas, name='areas'),
    path('area_cadastrar/', area_cadastrar, name='area_cadastrar'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('area_remover/<int:id>', area_remover, name='area_remover'),

    #==== PÚBLICO ====
    path('publicos/', publicos, name='publicos'),
    path('publico_cadastrar/', publico_cadastrar, name='publico_cadastrar'),
    path('publico_editar/<int:id>/', publico_editar, name='publico_editar'),
    path('publico_remover/<int:id>', publico_remover, name='publico_remover'),

    #==== CURSO ====
    path('cursos/', cursos, name='cursos'),
    path('curso_cadastrar/', curso_cadastrar, name='curso_cadastrar'),
    path('curso_editar/<int:id>/', curso_editar, name='curso_editar'),
    path('curso_remover/<int:id>', curso_remover, name='curso_remover'),


]