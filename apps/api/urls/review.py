from django.urls import path
from apps.api.views import review as review_views

urlpatterns = [
    path('location/<location>/', review_views.ReviewList.as_view()),
    path('location/<location>/my-review/',
         review_views.ReviewDetails.as_view()),
]
