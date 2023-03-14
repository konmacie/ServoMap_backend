from rest_framework import serializers
from apps.locations.models import Report


class ReportCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('user', 'location', 'message')
