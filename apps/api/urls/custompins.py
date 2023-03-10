from django.urls import path
from apps.api.views import custompin as custompin_views

urlpatterns = [
    path('list/', custompin_views.CustomPinList.as_view()),
    path('details/<pk>/', custompin_views.CustomPinDetail.as_view()),
]
