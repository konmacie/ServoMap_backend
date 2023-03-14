from rest_framework import serializers
from apps.locations.models import Location, LocationType


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

    rating_avg = serializers.DecimalField(
        max_digits=3, decimal_places=2, read_only=True)

    reviews_count = serializers.IntegerField(read_only=True)

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
