from rest_framework.response import Response

from apps.accounts.utils.validators.email_validator import EmailAddressValidator
from apps.accounts.utils.verification_code_manager import VerificationCodeManager
from apps.utils.constants.messages import Alerts, Success
from apps.utils.exceptions.api_exceptions import APIExceptions
from apps.utils.policy.brute_force_manager import BruteForceManager
from apps.utils.user_client import UserClient

from .base_strategy import ActivationBaseStrategy


class EmailActivationStrategy(ActivationBaseStrategy):
    def activate(self):
        validator = EmailAddressValidator(self.request)
        if validator.validate():
            user_client = UserClient(self.request)
            brute_force_manager = BruteForceManager(
                user_client.ip_address, "email_activation"
            )
            email = self.request.data.get("email", None)
            manager = VerificationCodeManager(email)
            if manager.value != self.request.data.get(
                       "verification_code", None):
                brute_force_manager.check_brute_force(
                    Alerts.INVALID_VERIFICATION_CODE, 400)

            profile = self.request.user.profile
            profile.email = email
            profile.is_email_activated = True
            profile.save()

            return Response({"message": Success.SUCCESSFULLY_ACTIVATED}, 200)
        else:
            raise APIExceptions(Alerts.INVALID_EMAIL_ADDRESS, 400)
