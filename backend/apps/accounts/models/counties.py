from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class Counties(UUIDMixin, TimeStampedMixin):
    county = models.CharField(
        verbose_name=_("County name"),
        max_length=100,
        blank=True,
        null=True,
    )
    zipcode = models.CharField(
        verbose_name=_("ZipCode"),
        max_length=20,
        default='',
    )
