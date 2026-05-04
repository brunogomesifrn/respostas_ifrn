from django.urls import path
from .views import *

urlpatterns = [
    path('', inicial, name='inicial'),
    path('curso_galeria/', curso_galeria, name='curso_galeria'),
]