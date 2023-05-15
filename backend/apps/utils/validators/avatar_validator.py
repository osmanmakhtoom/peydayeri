import logging
import os

from django.utils.deconstruct import deconstructible
from apps.utils.exceptions.custom_exceptions import (InvalidFileExtensionException,
                                                InvalidFileSizeException)

logger = logging.getLogger(__name__)


@deconstructible
class AvatarValidator:

    __valid_extensions = [
        ".jpg",
        ".png",
        ".gif",
        ".webp",
    ]

    def __call__(self, file_name):
        self.__file_extension = os.stat(file_name).st_type
        self.__file_size = os.stat(file_name).st_size / (1024 * 1024)
        if self.__file_extension not in self.__valid_extensions:
            logger.error("File extension not valid")
            raise InvalidFileExtensionException(self.__file_extension)
        if self.__file_size > 2:
            logger.error("File size too large")
            raise InvalidFileSizeException(self.__file_size)

    def __eq__(self, other):
        return isinstance(other, self.__class__)
