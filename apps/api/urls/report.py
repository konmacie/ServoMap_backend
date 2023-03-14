from django.urls import path
from apps.api.views import report as report_views

urlpatterns = [
    path('', report_views.ReportCreateAPIView.as_view()),
]
