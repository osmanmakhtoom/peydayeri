from apps.utils.policy.cache_manager import CacheManager


class VerificationCodeManager(CacheManager):
    def __init__(self, key: str):
        super().__init__(f"{key}_verification_code")
