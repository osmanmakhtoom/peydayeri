from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from apps.accounts.utils.request_processor import RequestProcessor


class RegisterViewSet(ViewSet):
    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def register(self, request):
        processor = RequestProcessor(request, "registration")
        return processor.process_registration_request()
