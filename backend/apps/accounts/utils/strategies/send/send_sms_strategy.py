from ippanel import Client
from rest_framework.response import Response

from django.conf import settings

from apps.accounts.utils.validators.phone_number_validator import \
    PhoneNumberValidator
from apps.accounts.utils.verification_code_manager import VerificationCodeManager
from django.conf import settings
from apps.utils.constants.messages import Alerts, Success, Warnings
from apps.utils.exceptions.api_exceptions import APIExceptions

from .base_strategy import SendActivationCodeBaseStrategy


class SendSMSStrategy(SendActivationCodeBaseStrategy):
    def send_activation_code(self, verification_code: str) -> Response:
        validator = PhoneNumberValidator(self.request)
        if validator.validate():
            phone = self.request.data.get("phone", None)
            manager = VerificationCodeManager(phone)
            if not manager.is_expired:
                raise APIExceptions(
                    Warnings.TRY_AGAIN_AFTER_2_MINUTES, 400)
            client = Client(settings.SMS_CLIENT_CODE)
            pattern_values = {
                "name": self.request.user.profile.firstname or
                self.request.user.username,
                "verification-code": verification_code,
            }
            try:
                client.send_pattern(
                    settings.SMS_CLIENT_ID, settings.SMS_PHONE_NUMBER, str(phone), pattern_values
                )
                manager = VerificationCodeManager(phone)
                manager.period = 120
                manager.value = verification_code
                return Response(
                    {"message": Success.CODE_SENT_SUCCESSFULLY}, 200)
            except Exception:
                raise APIExceptions(Alerts.CODE_SENDING_FAILED, 500)
        else:
            raise APIExceptions(Alerts.INVALID_PHONE_NUMBER, 400)
