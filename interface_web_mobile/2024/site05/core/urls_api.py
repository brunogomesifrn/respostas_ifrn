from django.urls import path
from .views import areaAPIlistar, areaAPIadicionar, areaAPIatualizar, areaAPIremover

urlpatterns = [
    path('areas/listar/', areaAPIlistar),
    path('areas/adicionar/', areaAPIadicionar),
    path('areas/atualizar/<int:id>/', areaAPIatualizar),
    path('areas/remover/<int:id>/', areaAPIremover),
]