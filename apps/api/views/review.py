from django.http import Http404
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response

from apps.api.serializers.review import ReviewSerializer
from apps.locations.models.review import Review


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('created', 'rating')

    def get_queryset(self):
        location = self.kwargs['location']
        return Review.objects.filter(location=location)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'location'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            # return empty response if review does not exist
            # prevent 404 error
            return Response({'id': None})
