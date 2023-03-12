from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="reviews"
    )

    location = models.ForeignKey(
        "Location",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="reviews"
    )

    rating = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    text = models.TextField(blank=True, null=True, max_length=512)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        unique_together = (("user", "location"),)
        ordering = ("-created",)

    def __str__(self):
        return f"{self.user} - {self.location} - {self.rating}"
