from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Addresses(models.Model):
    class TYPES(models.IntegerChoices):
        FACTOR = (1, "factor")
        DELIVER = (2, "deliver")

    user = models.ForeignKey(
        verbose_name=_("Related user"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='addresses',
    )
    country = models.CharField(
        verbose_name=_("Country name"),
        max_length=100,
        blank=True,
        null=True,
    )
    state = models.CharField(
        verbose_name=_("County name"),
        max_length=100,
        blank=True,
        null=True,
    )
    city = models.CharField(
        verbose_name=_("City name"),
        max_length=100,
        null=True,
        blank=True,
    )
    village = models.CharField(
        verbose_name=_("Village name"),
        max_length=100,
        default='',
    )
    zipcode = models.CharField(
        verbose_name=_("ZipCode"),
        max_length=20,
        default='',
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
        verbose_name=_("Address type, Factor or deliver?"),
        choices=TYPES,
        default=TYPES.FACTOR,
    )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
