from django_filters import rest_framework as filters

from apps.locations.models import Location, LocationType


class LocationFilter(filters.FilterSet):
    """
    Filter locations by provided bounds.
    Required filters:
        'longitude__gte', 'longitude__lt', 'latitude__gte', 'latitude__lt'.
    Optional filters:
        'type'.
    """
    type = filters.ModelMultipleChoiceFilter(
        queryset=LocationType.objects.all(),
        field_name='type',
    )
    longitude__gte = filters.NumberFilter(
        field_name='longitude',
        lookup_expr='gte',
        required=True
    )
    longitude__lt = filters.NumberFilter(
        field_name='longitude',
        lookup_expr='lt',
        required=True
    )
    latitude__gte = filters.NumberFilter(
        field_name='latitude',
        lookup_expr='gte',
        required=True
    )
    latitude__lt = filters.NumberFilter(
        field_name='latitude',
        lookup_expr='lt',
        required=True
    )

    class Meta:
        model = Location
        fields = ['type', 'longitude__gte', 'longitude__lt',
                  'latitude__gte', 'latitude__lt']
        # fields = {
        #     'longitude': ['gt', 'gte', 'lt', 'lte'],
        #     'latitude': ['gt', 'gte', 'lt', 'lte'],
        # }
