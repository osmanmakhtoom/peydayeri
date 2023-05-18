from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class TimeZones(UUIDMixin, TimeStampedMixin):
    timezone = models.CharField(
        verbose_name=_("TimeZone code"),
        max_length=6,
        blank=True,
        null=True,
    )
