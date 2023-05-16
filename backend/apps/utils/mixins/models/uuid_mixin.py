import uuid as uuid_lib

from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        verbose_name=_("Unique ID"),
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True
