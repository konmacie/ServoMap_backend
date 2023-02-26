from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.template.defaultfilters import truncatechars


class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reports'
    )

    location = models.ForeignKey(
        to='Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reports'
    )

    message = models.TextField(
        verbose_name=_('Message'),
        blank=False,
        max_length=512,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )

    @property
    def message_truncated(self):
        return truncatechars(self.message, 100)

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')

    def __str__(self):
        return self.message
