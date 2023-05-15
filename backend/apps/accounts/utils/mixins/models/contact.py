from django.db import models
from apps.utils.validators.phone_validator import PhoneValidator


class ContactInformationMixin(models.Model):
    phone_validator = PhoneValidator()

    phone = models.CharField(
        max_length=15,
        blank=True,
        validators=[
            phone_validator,
        ],
    )
    is_phone_activated = models.BooleanField(default=False)
    email = models.EmailField(blank=True)
    is_email_activated = models.BooleanField(default=False)

    class Meta:
        abstract = True
