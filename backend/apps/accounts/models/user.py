from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers.user_manager import UserManager
from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class User(AbstractBaseUser, UUIDMixin, TimeStampedMixin, PermissionsMixin):
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=100,
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("Is user activated?"),
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_("Is staff?"),
        default=False,
    )
    is_store = models.BooleanField(
        verbose_name=_("Is store account?"),
        default=False,
    )

    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
