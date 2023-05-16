import logging
from io import BytesIO

import arrow
import requests
from PIL import Image

from django.core.files import File
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.validators.avatar_validator import AvatarValidator

logger = logging.getLogger(__name__)


class PersonalDetailsMixin(models.Model):
    class GENDER(models.IntegerChoices):
        MALE = (1, "male")
        FEMALE = (2, "female")
        NOT_SPECIFIED = (3, "not specified")

    avatar_validator = AvatarValidator()

    firstname = models.CharField(
        verbose_name=_("First name"),
        max_length=150,
        null=True,
        default="",
    )
    lastname = models.CharField(
        verbose_name=_("Last name"),
        max_length=150,
        null=True,
        default="",
    )
    avatar = models.ImageField(
        verbose_name=_("Profile picture"),
        upload_to="avatars/%Y/%M/%D/",
        null=True,
        blank=True,
        validators=[
            avatar_validator,
        ],
    )
    avatar_url = models.URLField(
        verbose_name=_("Profile picture URL if from another resource"),
        null=True,
        default=None,
    )
    date_of_born = models.DateTimeField(
        verbose_name=_("Birthdate"),
        blank=True,
        null=True,
    )
    country = models.CharField(
        verbose_name=_("Country"),
        max_length=100,
        blank=True,
        null=True,
    )
    state = models.CharField(
        verbose_name=_("County"),
        max_length=100,
        blank=True,
        null=True,
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=100,
        null=True,
        blank=True,
    )
    address = models.TextField(
        verbose_name=_("Full address"),
        blank=True,
        null=True,
    )
    timezone = models.CharField(
        verbose_name=_("TimeZone"),
        max_length=6,
        blank=True,
        null=True,
    )
    gender = models.IntegerField(
        verbose_name=_("Gender"),
        choices=GENDER,
        default=GENDER.MALE,
    )
    language = models.CharField(
        verbose_name=_("Native language code"),
        max_length=6,
        blank=True,
        null=True,
        default="fa",
    )

    class Meta:
        abstract = True

    @property
    def short_name(self):
        return self.firstname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def age(self):
        if self.date_of_born:
            now = arrow.get(arrow.now(), "YYYY-MM-DD HH:mm:ss")
            birth_date = arrow.get(self.date_of_born, "YYYY-MM-DD HH:mm:ss")
            return now - birth_date

    def get_remote_image(self):
        if self.avatar_url and not self.avatar:
            try:
                result = requests.get(
                    self.avatar_url, allow_redirects=True).content
                cached_image = BytesIO(result)
                self.avatar = cached_image
                self.save()
            except requests.HTTPError as e:
                logger.error(e.msg)

    def reduce_avatar_size(self, avatar):
        image = Image.open(avatar)
        thumb_io = BytesIO()
        image.save(thumb_io, "JPEG", optimize=True, quality=80)
        new_image = File(thumb_io, name=f"{self.user.username}-avatar.jpg")
        return new_image
