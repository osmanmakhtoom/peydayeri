from enum import Enum

from django.utils.translation import gettext_lazy as _


class General(str, Enum):
    VERIFICATION_CODE_EMAIL_SUBJECT = _(
        "peydayeri_verification_code_subject")
    VERIFICATION_CODE_EMAIL_BODY = _(
        "peydayeri_verification_code_body")
    INFO_EMAIL_ADDRESS = "info@osman-makhtoom.ir"


class Success(str, Enum):
    CODE_SENT_SUCCESSFULLY = _("verification_code_sent")
    SUCCESSFULLY_ACTIVATED = _("successfully_verified")
    PLEASE_ENTER_YOUR_PASSWORD = _("enter_password")
    LOGGED_IN_SUCCESSFULLY = _("logged_in")
    REGISTERED_SUCCESSFULLY = _("registered")
    LOGGED_OUT_SUCCESSFULLY = _("logged_out")


class Alerts(str, Enum):
    CODE_SENDING_FAILED = _("verification_code_sending_failed")
    LOGGING_IN_FAILED = _("login_failed")
    REGISTERING_FAILED = _("registration_failed")
    LOGGING_OUT_FAILED = _("logout_failed")
    USER_WITH_THIS_PHONE_NUMBER_NOT_FOUND = _("phone_number_not_found")
    INVALID_CREDENTIALS = _("invalid_credentials")
    YOUR_ACCOUNT_LOCKED = _("account_locked_out")
    YOUR_IP_ADDRESS_LOCKED = _("ip_address_locked_out")
    USER_NAME_IS_REQUIRED = _("username_required")
    INVALID_PHONE_NUMBER = _("invalid_phone_number")
    INVALID_EMAIL_ADDRESS = _("invalid_email_address")
    INVALID_VERIFICATION_CODE = _("invalid_verification_code")
    INVALID_FILE_EXTENSION = _("invalid_file_extension")
    INVALID_FILE_SIZE = _("invalid_file_size")
    YOU_ARE_ALREADY_LOGGED_IN = _("you_are_already_logged_in")
    PHONE_NUMBER_ALREADY_ACTIVATED = _("phone_number_already_activated")
    EMAIL_ALREADY_ACTIVATED = _("email_already_activated")


class Warnings(str, Enum):
    TRY_AGAIN_AFTER_2_MINUTES = _("try_again_after_2_minutes")
    TRY_AGAIN_AFTER_5_MINUTES = _("try_again_after_5_minutes")
    YOUR_ACCOUNT_WILL_LOCKED_AFTER_3_INVALID_ATTEMPTS = _(
        "account_will_lock_after_3_invalid_attempts"
    )
    USER_WITH_THIS_PHONE_NUMBER_ALREADY_EXIST = _("user_already_exist")
    VERIFICATION_CODE_EXPIRED = _("verification_code_expired")
