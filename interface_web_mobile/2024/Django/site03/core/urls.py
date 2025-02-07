from django.urls import path, include
from .views import home, cadastro, cadastro_resultado

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro_resultado/', cadastro_resultado, name='cadastro_resultado'),
    
]
