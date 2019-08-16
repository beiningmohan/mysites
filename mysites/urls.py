from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('control/', admin.site.urls),
]
