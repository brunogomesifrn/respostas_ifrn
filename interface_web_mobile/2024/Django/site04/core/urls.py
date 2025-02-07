from django.urls import path
from .views import areas, area_cadastro, area_editar, area_remover

urlpatterns = [
    path('areas/', areas, name='areas'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),

]