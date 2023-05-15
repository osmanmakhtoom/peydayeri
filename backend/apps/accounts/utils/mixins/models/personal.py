import logging
from io import BytesIO

import arrow
import requests
from PIL import Image

from django.core.files import File
from django.db import models
from apps.utils.validators.avatar_validator import AvatarValidator

logger = logging.getLogger(__name__)


class PersonalDetailsMixin(models.Model):
    avatar_validator = AvatarValidator()

    firstname = models.CharField(max_length=150, null=True, default="")
    lastname = models.CharField(max_length=150, null=True, default="")
    avatar = models.ImageField(
        upload_to="avatars/%Y/%M/%D/",
        null=True,
        blank=True,
        validators=[
            avatar_validator,
        ],
    )
    avatar_url = models.URLField(null=True, default=None)
    date_of_born = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=6, blank=True, null=True)
    language = models.CharField(
        max_length=6, blank=True, null=True, default="fa")

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
