from abc import ABC, abstractmethod

from django.http.request import HttpRequest


class BaseValidator(ABC):
    def __init__(self, request: HttpRequest) -> None:
        self._request = request

    @property
    def request(self) -> str:
        return self._request

    @request.setter
    def request(self, request: str) -> None:
        self._request = request

    @abstractmethod
    def validate(self) -> bool:
        raise NotImplementedError
