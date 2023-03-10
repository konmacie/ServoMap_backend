from rest_framework import generics
from rest_framework import permissions

from apps.api.serializers.custompin import CustomPinSerializer
from apps.api.permissions import IsOwner


class CustomPinList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomPinSerializer

    def get_queryset(self):
        return self.request.user.custom_pins.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# TODO: Add view with coordinates filtering


class CustomPinDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner
    ]
    serializer_class = CustomPinSerializer

    def get_queryset(self):
        return self.request.user.custom_pins.all()
