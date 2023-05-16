from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.validators.phone_validator import PhoneValidator


class ContactInformationMixin(models.Model):
    phone_validator = PhoneValidator()

    phone = models.CharField(
        verbose_name=_("Phone number"),
        max_length=15,
        blank=True,
        validators=[
            phone_validator,
        ],
    )
    is_phone_activated = models.BooleanField(
        verbose_name=_("Is phone number activated?"),
        default=False,
    )
    email = models.EmailField(
        verbose_name=_("Email address"),
        blank=True,
    )
    is_email_activated = models.BooleanField(
        verbose_name=_("Is email address activated?"),
        default=False,
    )

    class Meta:
        abstract = True
