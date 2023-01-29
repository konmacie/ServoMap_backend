from django.contrib import admin
from .models import Location, LocationType


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('id', 'name', 'type', 'latitude', 'longitude')
    list_filter = ('type',)
    ordering = ('id',)


# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType)
