from django.core.exceptions import RequestDataTooBig, ValidationError
from backend.apps.utils.constants.messages import Alerts


class InvalidPhoneNumberException(ValidationError):
    def __init__(self, phone_number="", message=Alerts.INVALID_PHONE_NUMBER.value):
        self.phone_number = phone_number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Phone number: {self.phone_number} -> {self.message}"


class InvalidFileExtensionException(ValidationError):
    def __init__(self, file_extension="",
                 message=Alerts.INVALID_FILE_EXTENSION.value):
        self.file_extension = file_extension
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"File Extension: {self.file_extension} -> {self.message}"


class InvalidFileSizeException(RequestDataTooBig):
    def __init__(self, file_size="", message=Alerts.INVALID_FILE_SIZE.value):
        self.file_size = file_size
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"File size: {self.file_size} -> {self.message}"
