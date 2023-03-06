from django.contrib import admin
from django.urls import path, include
from apps.api import views

urlpatterns = [
    path('locations/', include('apps.api.urls.locations')),
    path('accounts/', include('apps.api.urls.accounts')),
]
