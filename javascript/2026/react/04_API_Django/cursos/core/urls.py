from django.urls import path
from .views import *

urlpatterns = [
   path('areas/listar/', AreasListarAPI, name='AreasListarAPI'),
   path('areas/inserir/', AreaInserirAPI, name='AreaInserirAPI'),
   path('areas/editar/<int:id>/', AreaEditarAPI, name="AreaEditarAPI"),
]