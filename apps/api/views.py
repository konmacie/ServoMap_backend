from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics

from apps.locations.models import LocationType, Location
from .serializers import (LocationTypeSerializer, LocationSerializer,
                          LocationDetailsSerializer, ReportCreateSerializer)
from .filters import LocationFilter


@method_decorator(ensure_csrf_cookie, name='dispatch')
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


class ReportCreateAPIView(generics.CreateAPIView):
    serializer_class = ReportCreateSerializer

    def perform_create(self, serializer):
        if (self.request.user.is_authenticated):
            serializer.save(user=self.request.user)
        else:
            serializer.save()
