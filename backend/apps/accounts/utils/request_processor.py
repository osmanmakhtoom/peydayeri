import random
from typing import Dict

from rest_framework.response import Response

from apps.accounts.models.user import User
from apps.accounts.utils.strategies.activate.email_activation_strategy import \
    EmailActivationStrategy
from apps.accounts.utils.strategies.activate.phone_activation_strategy import \
    PhoneActivationStrategy
from apps.accounts.utils.strategies.send.send_mail_strategy import SendMailStrategy
from apps.accounts.utils.strategies.send.send_sms_strategy import SendSMSStrategy
from django.http.request import HttpRequest
from apps.utils.constants.messages import Alerts, Success, Warnings
from apps.utils.exceptions.api_exceptions import APIExceptions
from apps.utils.policy.brute_force_manager import BruteForceManager
from apps.utils.user_client import UserClient


class RequestProcessor:
    def __init__(self, request: HttpRequest, action: str) -> None:
        self._request = request
        self._action = action

    @property
    def request(self) -> HttpRequest:
        return self._request

    @request.setter
    def request(self, request: HttpRequest) -> None:
        self._request = request

    @property
    def key_lowered_data(self) -> Dict:
        return dict((k.lower(), v) for k, v in self.request.data.items())

    def process_registration_request(self) -> Response:
        """ Register user if not already have an account """
        if self.request.user.is_authenticated:
            raise APIExceptions(Alerts.YOU_ARE_ALREADY_LOGGED_IN.value, 400)
        user = User.objects.filter(
            username=self.key_lowered_data.get("username"))[0]
        if user:
            user_client = UserClient(self.request)
            brute_force_manager = BruteForceManager(
                user_client.ip_address, self._action)
            brute_force_manager.check_brute_force(
                Warnings.USER_WITH_THIS_PHONE_NUMBER_ALREADY_EXIST.value, 400)
        User.objects.create_user(
            self.key_lowered_data.get("username"),
            self.key_lowered_data.get("password")
        )
        return Response({"message": Success.REGISTERED_SUCCESSFULLY.value}, 201)

    def process_send_activation_request(self, manner: str) -> Response:
        """ Send verification code using the given manner """
        result = {
            "sms": SendSMSStrategy,
            "email": SendMailStrategy,
        }.get(manner, SendSMSStrategy)(self.request)
        verification_code = str(random.randint(111111, 999999))
        return result.send_activation_code(verification_code)

    def process_activation_request(self, manner: str) -> Response:
        """ Manage user verification requests using the given manner """
        result = {
            "email": EmailActivationStrategy,
            "phone": PhoneActivationStrategy,
        }.get(manner, SendSMSStrategy)(self.request)
        return result.activate()
