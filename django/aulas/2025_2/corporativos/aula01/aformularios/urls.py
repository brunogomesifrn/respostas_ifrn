from django.urls import path
from .views import cadastro, dados

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('dados/', dados, name='dados'),
]