from django.http.request import HttpRequest
from apps.utils.constants.messages import Alerts
from apps.utils.exceptions.api_exceptions import APIExceptions
from apps.utils.policy.brute_force_manager import BruteForceManager
from apps.utils.user_client import UserClient
from apps.utils.validators.phone_validator import PhoneValidator

from .base_validator import BaseValidator


class PhoneNumberValidator(BaseValidator):
    def __init__(self, request: HttpRequest) -> None:
        super().__init__(request)

    def validate(self) -> bool:
        user_client = UserClient(self.request)
        brute_force_manager = BruteForceManager(
            user_client.ip_address, "phone_activation"
        )
        if brute_force_manager.is_locked:
            raise APIExceptions(Alerts.YOUR_IP_ADDRESS_LOCKED.value, 403)

        phone = self.request.data.get("phone", None)
        validator = PhoneValidator()

        if phone is None or validator(phone) is False:
            brute_force_manager.check_brute_force(
                Alerts.INVALID_PHONE_NUMBER.value, 400)

        if (
            phone == self.request.user.profile.phone
            and self.request.user.profile.is_phone_activated
        ):
            brute_force_manager.check_brute_force(
                Alerts.PHONE_NUMBER_ALREADY_ACTIVATED.value, 400)

        return True
