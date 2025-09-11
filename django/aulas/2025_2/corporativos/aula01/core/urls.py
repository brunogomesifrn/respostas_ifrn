from django.urls import path
from .views import index, contato

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
]