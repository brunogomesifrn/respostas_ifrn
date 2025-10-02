from django.urls import path
from .views import areas

urlpatterns = [
    path('areas/', areas, name='areas'),
]

