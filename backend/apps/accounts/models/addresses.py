from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class Addresses(UUIDMixin, TimeStampedMixin):
    class TYPES(models.IntegerChoices):
        HOME = (1, "home")
        FACTOR = (2, "factor")
        DELIVER = (3, "deliver")

    user = models.ForeignKey(
        verbose_name=_("Related user"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='addresses',
    )
    timezone = models.ForeignKey(
        verbose_name=_("TimeZone"),
        to="apps.accounts.TimeZones",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    country = models.ForeignKey(
        verbose_name=_("Country"),
        to="apps.accounts.Countries",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    county = models.ForeignKey(
        verbose_name=_("County"),
        to="apps.accounts.Counties",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        verbose_name=_("City"),
        to="apps.accounts.Cities",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    village = models.ForeignKey(
        verbose_name=_("Village"),
        to="apps.accounts.Villages",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    address = models.TextField(
        verbose_name=_("Full address"),
        blank=True,
        null=True,
    )
    name = models.CharField(
        verbose_name=_("Receiver name"),
        max_length=255,
        null=True,
        default='',
    )
    type = models.IntegerField(
        verbose_name=_("Address type, Home, Factor or deliver?"),
        choices=TYPES,
        default=TYPES.HOME,
    )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
