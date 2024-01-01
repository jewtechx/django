from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('fundamentalsApp.urls')),
    path('admin/', admin.site.urls),
]
