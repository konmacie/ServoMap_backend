from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from decimal import Decimal


class CustomPin(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Owner'),
        on_delete=models.CASCADE,
        null=False,
        related_name='custom_pins',
    )

    label = models.CharField(
        max_length=60,
        verbose_name=_('Label')
    )

    description = models.TextField(
        verbose_name=_(
            'Description'),
        blank=True,
        max_length=255
    )

    latitude = models.DecimalField(
        _("Latitude"),
        max_digits=12,
        decimal_places=9,
        validators=[
            MinValueValidator(Decimal(settings.MIN_LATITUDE)),
            MaxValueValidator(Decimal(settings.MAX_LATITUDE)),
        ]
    )
    longitude = models.DecimalField(
        _("Longitude"),
        max_digits=12,
        decimal_places=9,
        validators=[
            MinValueValidator(Decimal(settings.MIN_LONGITUDE)),
            MaxValueValidator(Decimal(settings.MAX_LONGITUDE)),
        ]
    )

    icon = models.CharField(max_length=60, verbose_name=_('Icon'), blank=True)

    # TODO: Add validation for icon
    # ? Maybe add public pins?

    class Meta:
        verbose_name = _("Custom pin")
        verbose_name_plural = _("Custom pins")

    def __str__(self):
        return self.label
