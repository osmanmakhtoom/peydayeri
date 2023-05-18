from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class Cities(UUIDMixin, TimeStampedMixin):
    city = models.CharField(
        verbose_name=_("City name"),
        max_length=100,
        null=True,
        blank=True,
    )
