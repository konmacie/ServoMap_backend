from rest_framework import serializers
from apps.locations.models import CustomPin


class CustomPinSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CustomPin
        fields = '__all__'
