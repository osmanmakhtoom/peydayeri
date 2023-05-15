from abc import ABC, abstractmethod

from rest_framework.response import Response

from django.http.request import HttpRequest


class ActivationBaseStrategy(ABC):
    def __init__(self, request: HttpRequest) -> None:
        self.request = request

    @abstractmethod
    def activate(self) -> Response:
        raise NotImplementedError
