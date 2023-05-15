import logging

import arrow

from apps.utils.constants.messages import Alerts
from apps.utils.exceptions.api_exceptions import APIExceptions
from apps.utils.policy.cache_manager import CacheManager

logger = logging.getLogger(__name__)


class BruteForceManager(CacheManager):
    def __init__(self, ip_or_username: str, level: str):
        self.__level = level
        super().__init__(f"{level}_invalid_attempt_{ip_or_username}")

    @property
    def level(self) -> str:
        return self.__level

    @property
    def is_locked(self) -> bool:
        try:
            if self.value and self.value.get("lockout_start"):
                lockout_start = arrow.get(self.value.get("lockout_start"))
                locked_out = lockout_start >= arrow.now().shift(minutes=-60)
                if not locked_out:
                    self.delete()
                    return False
                else:
                    return True
            else:
                return False
        except Exception as e:
            logger.error(e)
            return False

    def set_new_timestamp(self):
        if not self.is_locked:
            lockout_timestamp = None
            invalid_attempt_timestamps = (
                self.value.get(
                    "invalid_attempt_timestamps") if self.value else []
            )
            invalid_attempt_timestamps = [
                timestamp_item
                for timestamp_item in invalid_attempt_timestamps
                if timestamp_item > arrow.now().shift(minutes=-60).timestamp()
            ]
            invalid_attempt_timestamps.append(arrow.now().timestamp())
            if len(invalid_attempt_timestamps) == 3:
                lockout_timestamp = arrow.now().timestamp()

            self.value = {
                "lockout_start": lockout_timestamp,
                "invalid_attempt_timestamps": invalid_attempt_timestamps,
            }

    def check_brute_force(self, msg: str, code: int) -> None:
        """ Checks if the IP address is blocked """
        if not self.is_locked:
            self.set_new_timestamp()
            raise APIExceptions(msg, code)
        else:
            raise APIExceptions(Alerts.YOUR_IP_ADDRESS_LOCKED, 403)
