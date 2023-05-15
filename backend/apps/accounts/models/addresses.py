from django.db import models
from django.conf import settings


class Addresses(models.Model):
    class TYPES(models.IntegerChoices):
        FACTOR = (1, "factor")
        DELIVER = (2, "deliver")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    village = models.CharField(max_length=255, default='')
    county = models.CharField(max_length=255, default='')
    zipcode = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, null=True, default=None)
    type = models.IntegerField(choices=TYPES, default=TYPES.FACTOR)
