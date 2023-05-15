from backend.apps.accounts.managers.user_manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.utils.mixins.models.timestamp import TimeStampedMixin
from apps.utils.mixins.models.uuid_mixin import UUIDMixin


class User(AbstractBaseUser, UUIDMixin, TimeStampedMixin, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()
