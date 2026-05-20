from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('curso_galeria/', curso_galeria, name='curso_galeria'),
]