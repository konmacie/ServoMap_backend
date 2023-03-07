from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from decimal import Decimal


class Location(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=False,
        null=False
    )
    type = models.ForeignKey(
        to="LocationType",
        verbose_name=_("Type"),
        on_delete=models.PROTECT,
        null=False,
    )
    latitude = models.DecimalField(
        _("Latitude"),
        max_digits=9,
        decimal_places=6,
        validators=[
            MinValueValidator(Decimal(settings.MIN_LATITUDE)),
            MaxValueValidator(Decimal(settings.MAX_LATITUDE)),
        ]
    )
    longitude = models.DecimalField(
        _("Longitude"),
        max_digits=9,
        decimal_places=6,
        validators=[
            MinValueValidator(Decimal(settings.MIN_LONGITUDE)),
            MaxValueValidator(Decimal(settings.MAX_LONGITUDE)),
        ]
    )
    address = models.CharField(
        _("Address"),
        max_length=255,
        blank=True,
    )
    city = models.CharField(
        _("City"),
        max_length=100,
        blank=True,
    )
    postal_code = models.CharField(
        _("Postal Code"),
        max_length=10,
        blank=True,
    )

    favourite = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="favourites",
    )

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.name
