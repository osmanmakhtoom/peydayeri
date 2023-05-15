from abc import ABC, abstractmethod

from rest_framework.response import Response

from django.http.request import HttpRequest


class SendActivationCodeBaseStrategy(ABC):
    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    @abstractmethod
    def send_activation_code(self, verification_code: str) -> Response:
        raise NotImplementedError
