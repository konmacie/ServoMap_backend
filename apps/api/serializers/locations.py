from rest_framework import serializers
from apps.locations.models import Location, LocationType, Report, CustomPin


class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = '__all__'


class LocationShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'type', 'latitude', 'longitude']


class LocationDetailsSerializer(serializers.ModelSerializer):
    type = LocationTypeSerializer(read_only=True)
    favourited = serializers.SerializerMethodField()

    def get_favourited(self, obj):
        favourited = False
        request = self.context['request']
        if request and request.user.is_authenticated:
            user = request.user
            favourited = obj.favourite.filter(pk=user.pk).exists()
        return favourited

    class Meta:
        model = Location
        # fields = '__all__'
        exclude = ['favourite']


class ReportCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('user', 'location', 'message')
