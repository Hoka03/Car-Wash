from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('washing/', include('apps.washing.urls')),
    path('cars/', include('apps.cars.urls')),
]
