import logging

from rest_framework.exceptions import APIException

logger = logging.getLogger(__name__)


class APIExceptions(APIException):
    detail = None
    status_code = None

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.detail = detail
        self.status_code = code
        logger.error(detail)
