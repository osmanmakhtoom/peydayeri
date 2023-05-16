from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class SocialAccounts(UUIDMixin, TimeStampedMixin):
    user = models.ForeignKey(
        verbose_name=_("Related user"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        related_name='social_accounts',
    )
    network_name = models.CharField(
        verbose_name=_("Social network name"),
        max_length=20,
    )
    network_user_name = models.CharField(
        verbose_name=_("Social network ID"),
        max_length=25,
    )

    class Meta:
        unique_together = ["user", "network_name"]
        verbose_name = _("Social account")
        verbose_name_plural = _("Social accounts")
