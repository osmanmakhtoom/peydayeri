from django.core.validators import EmailValidator
from apps.utils.constants.messages import Alerts
from apps.utils.exceptions.api_exceptions import APIExceptions
from apps.utils.policy.brute_force_manager import BruteForceManager
from apps.utils.user_client import UserClient

from .base_validator import BaseValidator


class EmailAddressValidator(BaseValidator):
    def __init__(self, request: str) -> None:
        super().__init__(request)

    def validate(self) -> bool:
        email = self.request.data.get("email", None)
        validator = EmailValidator()

        user_client = UserClient(self.request)
        brute_force_manager = BruteForceManager(
            user_client.ip_address, "email_activation"
        )

        if brute_force_manager.is_locked:
            raise APIExceptions(Alerts.YOUR_IP_ADDRESS_LOCKED, 403)

        if email is None or validator(email) is False:
            brute_force_manager.check_brute_force(
                Alerts.INVALID_EMAIL_ADDRESS, 400)

        if (
            email == self.request.user.profile.email
            and self.request.user.profile.is_email_activated
        ):
            brute_force_manager.check_brute_force(
                Alerts.EMAIL_ALREADY_ACTIVATED, 400)

        return True
