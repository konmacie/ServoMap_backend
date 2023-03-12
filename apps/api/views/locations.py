from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.locations.models import LocationType, Location
from apps.api.serializers.locations import (
    LocationTypeSerializer, LocationShortSerializer, LocationDetailsSerializer,
    ReportCreateSerializer
)
from apps.api.filters import LocationFilter


class LocationTypeListAPIView(generics.ListAPIView):
    queryset = LocationType.objects.all()
    serializer_class = LocationTypeSerializer
    pagination_class = None


class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationShortSerializer
    filterset_class = LocationFilter


class LocationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationDetailsSerializer

    def get_queryset(self):
        qs = Location.objects.annotate(
            rating_avg=Avg('reviews__rating'),
            reviews_count=Count('reviews')
        )
        return qs


class ReportCreateAPIView(generics.CreateAPIView):
    serializer_class = ReportCreateSerializer

    def perform_create(self, serializer):
        if (self.request.user.is_authenticated):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class FavouriteLocationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        location = get_object_or_404(
            Location, pk=kwargs.get('pk'))
        if request.user not in location.favourite.all():
            location.favourite.add(request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(
            {'details': "Location already favourited."},
            status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, *args, **kwargs):
        location = get_object_or_404(
            Location, pk=kwargs.get('pk'))
        if request.user in location.favourite.all():
            location.favourite.remove(request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(
            {'details': "Location not in favourites."},
            status.HTTP_400_BAD_REQUEST
        )
