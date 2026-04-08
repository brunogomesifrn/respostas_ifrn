from django.urls import path
from .views import inicial, contato

urlpatterns = [
    path('', inicial, name='inicial'),
    path('contato/', contato, name='contato'),
]