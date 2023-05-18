from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class Villages(UUIDMixin, TimeStampedMixin):
    village = models.CharField(
        verbose_name=_("Village name"),
        max_length=100,
        default='',
    )
