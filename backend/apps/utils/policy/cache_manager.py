import logging
from abc import ABC

from django.core.cache import cache

logger = logging.getLogger(__name__)


class CacheManager(ABC):

    def __init__(self, key: str):
        self.__key = key

    @property
    def key(self) -> str:
        return self.__key

    @property
    def value(self) -> any:
        return cache.get(self.key)

    @property
    def period(self) -> int:
        return self.__period

    @value.setter
    def value(self, value: any):
        cache.set(self.key, value, self.period)

    @period.setter
    def period(self, period: int):
        self.__period = period

    @property
    def is_expired(self) -> bool:
        try:
            if cache.get(self.key) is not None:
                return False
            return True
        except Exception as e:
            logger.error(e)
            return True

    def delete(self) -> bool:
        try:
            cache.delete(self.key)
            return True
        except Exception as e:
            logger.error(e)
            return False
