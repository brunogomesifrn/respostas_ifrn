from django.urls import path
from .views import AreasListarAPI

urlpatterns = [
   path('areas/listar/', AreasListarAPI, name='AreasListarAPI'),
]