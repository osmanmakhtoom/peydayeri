from enum import Enum

from django.utils.translation import gettext_lazy as _


class General(str, Enum):
    VERIFICATION_CODE_EMAIL_SUBJECT = _("Peydayeri verification code")
    VERIFICATION_CODE_EMAIL_BODY = _("Peydayeri verification code is below:")
    INFO_EMAIL_ADDRESS = "info@osman-makhtoom.ir"


class Success(str, Enum):
    CODE_SENT_SUCCESSFULLY = _("The verification code was sent successfully")
    SUCCESSFULLY_ACTIVATED = _("Your account is verified successfully")
    PLEASE_ENTER_YOUR_PASSWORD = _("Please enter your password")
    LOGGED_IN_SUCCESSFULLY = _("Successfully logged in")
    REGISTERED_SUCCESSFULLY = _("Successfully registered")
    LOGGED_OUT_SUCCESSFULLY = _("Successfully logged out")


class Alerts(str, Enum):
    CODE_SENDING_FAILED = _("Verification code sending failed")
    LOGGING_IN_FAILED = _("Login failed")
    REGISTERING_FAILED = _("Registration failed")
    LOGGING_OUT_FAILED = _("Logout failed")
    USER_WITH_THIS_PHONE_NUMBER_NOT_FOUND = _("Phone number not found")
    INVALID_CREDENTIALS = _("Invalid credentials")
    YOUR_ACCOUNT_LOCKED = _("Your account is locked out")
    YOUR_IP_ADDRESS_LOCKED = _("Your IP  address is Blocked")
    USER_NAME_IS_REQUIRED = _("Username is required")
    INVALID_PHONE_NUMBER = _("Invalid phone number")
    INVALID_EMAIL_ADDRESS = _("Invalid email address")
    INVALID_VERIFICATION_CODE = _("Invalid verification code")
    INVALID_FILE_EXTENSION = _("Invalid file extension")
    INVALID_FILE_SIZE = _("Invalid file size")
    YOU_ARE_ALREADY_LOGGED_IN = _("You are already logged in")
    PHONE_NUMBER_ALREADY_ACTIVATED = _("Phone number already activated")
    EMAIL_ALREADY_ACTIVATED = _("Email address already activated")


class Warnings(str, Enum):
    TRY_AGAIN_AFTER_2_MINUTES = _("Try again after 2 minutes")
    TRY_AGAIN_AFTER_5_MINUTES = _("Try again after 5 minutes")
    YOUR_ACCOUNT_WILL_LOCKED_AFTER_3_INVALID_ATTEMPTS = _(
        "Your account will lock after 3 invalid attempts"
    )
    USER_WITH_THIS_PHONE_NUMBER_ALREADY_EXIST = _("User already exists")
    VERIFICATION_CODE_EXPIRED = _("Verification code expired")
