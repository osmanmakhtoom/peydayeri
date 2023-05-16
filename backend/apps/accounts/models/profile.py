from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers.profile_manager import ProfileManager
from apps.accounts.utils.mixins.models.contact import ContactInformationMixin
from apps.accounts.utils.mixins.models.personal import PersonalDetailsMixin
from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class Profile(UUIDMixin, PersonalDetailsMixin, ContactInformationMixin,
              TimeStampedMixin):
    user = models.OneToOneField(
        verbose_name=_("Related user"),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    objects = ProfileManager()

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.avatar:
            avatar = self.reduce_avatar_size(self.avatar)
            self.avatar = avatar
        self.get_remote_image()
        super().save(*args, **kwargs)
