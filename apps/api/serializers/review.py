from rest_framework import serializers, validators
from apps.locations.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['user', 'location', 'rating', 'text', 'created']
        read_only_fields = ['user', 'location', 'created']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'location', 'rating', 'text']
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('user', 'location'),
            )
        ]
