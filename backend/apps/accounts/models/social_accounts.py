from django.conf import settings
from django.db import models
from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class SocialAccounts(UUIDMixin, TimeStampedMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        related_name='social_accounts')
    network_name = models.CharField(max_length=20)
    network_user_name = models.CharField(max_length=25)

    class Meta:
        unique_together = ["user", "network_name"]
