from django.contrib import admin
from .models import Location, LocationType, Report


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('id', 'name', 'type', 'latitude', 'longitude')
    list_filter = ('type',)
    ordering = ('id',)


class ReportAdmin(admin.ModelAdmin):
    model = Report
    list_display = ('user', 'location', 'message_truncated', 'created_at')
    list_display_links = ('message_truncated', 'created_at')


# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType)
admin.site.register(Report, ReportAdmin)
