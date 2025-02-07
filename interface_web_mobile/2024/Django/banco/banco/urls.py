from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('api/v1/', include('core.urls_api')),
    path('admin/', admin.site.urls),
]
