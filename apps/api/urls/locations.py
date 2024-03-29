from django.urls import path
from apps.api.views import locations as location_views

urlpatterns = [
    path('types/', location_views.LocationTypeListAPIView.as_view()),
    path('list/', location_views.LocationListAPIView.as_view()),
    path('details/<pk>/', location_views.LocationRetrieveAPIView.as_view()),
    path('details/<pk>/favourite/',
         location_views.FavouriteLocationAPIView.as_view()),
]
