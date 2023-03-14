from rest_framework import generics
from apps.api.serializers.report import ReportCreateSerializer


class ReportCreateAPIView(generics.CreateAPIView):
    serializer_class = ReportCreateSerializer

    def perform_create(self, serializer):
        if (self.request.user.is_authenticated):
            serializer.save(user=self.request.user)
        else:
            serializer.save()
