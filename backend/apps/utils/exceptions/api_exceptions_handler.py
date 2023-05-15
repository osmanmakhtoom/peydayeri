import arrow
from rest_framework.views import exception_handler


def api_exceptions_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data["message"] = response.data["detail"]
        response.data["time"] = arrow.now().format('YYYY-MM-DD HH:mm:ss ZZ')
        del response.data["detail"]
    return response
