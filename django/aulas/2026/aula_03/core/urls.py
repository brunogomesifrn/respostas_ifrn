from django.urls import path
from .views import inicio, contato

urlpatterns = [
    path('', inicio, name='inicio'),
    path('contato/', contato, name='contato'),
]
