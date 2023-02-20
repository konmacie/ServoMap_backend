from rest_framework import serializers
from apps.locations.models import Location, LocationType


class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class LocationDetailsSerializer(serializers.ModelSerializer):
    type = LocationTypeSerializer(read_only=True)

    class Meta:
        model = Location
        fields = '__all__'
