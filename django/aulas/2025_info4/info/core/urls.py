from django.urls import path
from .views import index, categorias
from .views import areas

urlpatterns = [
    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),

    path('areas/', areas, name='areas'),
]
