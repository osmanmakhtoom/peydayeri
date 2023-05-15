from django.db import models
import uuid as uuid_lib


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True
