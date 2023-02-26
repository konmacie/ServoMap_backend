from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('types/', views.LocationTypeListAPIView.as_view()),
    path('locations/', views.LocationListAPIView.as_view()),
    path('location/<pk>/', views.LocationRetrieveAPIView.as_view()),
    path('report/', views.ReportCreateAPIView.as_view()),
]
