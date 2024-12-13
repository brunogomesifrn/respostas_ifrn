from django.urls import path
from .views import areas, area_cadastro

urlpatterns = [
    path('areas/', areas, name='areas'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),
]