from django.db import models
from django.utils.translation import gettext_lazy as _


class LocationType(models.Model):
    name = models.CharField(_("Name"), max_length=50, blank=False, null=False)
    icon = models.CharField(_("Icon"), max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = _("Location type")
        verbose_name_plural = _("Location types")
        ordering = ('name',)

    def __str__(self):
        return self.name
