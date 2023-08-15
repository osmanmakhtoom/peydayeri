from rest_framework.response import Response

from apps.accounts.utils.validators.email_validator import EmailAddressValidator
from apps.accounts.utils.verification_code_manager import VerificationCodeManager
from django.core.mail import send_mail
from apps.utils.constants.messages import Alerts, General, Success, Warnings
from apps.utils.exceptions.api_exceptions import APIExceptions

from .base_strategy import SendActivationCodeBaseStrategy


class SendMailStrategy(SendActivationCodeBaseStrategy):
    def send_activation_code(self, verification_code: str) -> Response:
        """ Email verification code """
        validator = EmailAddressValidator(self.request)
        if validator.validate():

            email = self.request.data.get("email", None)
            manager = VerificationCodeManager(email)
            if not manager.is_expired:
                raise APIExceptions(Warnings.TRY_AGAIN_AFTER_5_MINUTES.value, 400)

            try:
                mail_send_result = send_mail(
                    General.VERIFICATION_CODE_EMAIL_SUBJECT.value,
                    General.VERIFICATION_CODE_EMAIL_BODY.value
                    + "\n" + verification_code,
                    from_email=General.INFO_EMAIL_ADDRESS.value,
                    recipient_list=[
                        email,
                    ],
                )
                if mail_send_result == 0:
                    raise APIExceptions(Alerts.CODE_SENDING_FAILED.value, 500)
                manager.period = 300
                manager.value = verification_code
                return Response(
                    {"message": Success.CODE_SENT_SUCCESSFULLY.value}, 200)
            except Exception:
                raise APIExceptions(Alerts.CODE_SENDING_FAILED.value, 500)
        else:
            raise APIExceptions(Alerts.INVALID_EMAIL_ADDRESS.value, 400)
