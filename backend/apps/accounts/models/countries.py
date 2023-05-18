from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class Countries(UUIDMixin, TimeStampedMixin):
    country = models.CharField(
        verbose_name=_("Country name"),
        max_length=100,
        blank=True,
        null=True,
    )
