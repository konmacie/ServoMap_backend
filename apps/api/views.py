from django.shortcuts import render
from rest_framework import generics

from apps.locations.models import LocationType, Location
from .serializers import (LocationTypeSerializer,
                          LocationSerializer, LocationDetailsSerializer)
from .filters import LocationFilter


class LocationTypeListAPIView(generics.ListAPIView):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    pagination_class = None


class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filterset_class = LocationFilter


class LocationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDetailsSerializer
