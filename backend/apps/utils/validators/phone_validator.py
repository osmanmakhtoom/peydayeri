import logging
import re

from django.utils.deconstruct import deconstructible
from apps.utils.exceptions.custom_exceptions import InvalidPhoneNumberException

logger = logging.getLogger(__name__)


@deconstructible
class PhoneValidator:
    def __call__(self, phone_number):
        if phone_number is None or (
                len(phone_number) < 11 or len(phone_number) > 15):
            logger.error("Phone number length is invalid")
            raise InvalidPhoneNumberException(phone_number)
        pattern = re.compile(r"((\+|00)98|0)9\d{9}")
        match = pattern.fullmatch(phone_number)
        if not match:
            logger.error("Phone number format is invalid")
            raise InvalidPhoneNumberException(phone_number)

    def __eq__(self, other):
        return isinstance(other, self.__class__)
