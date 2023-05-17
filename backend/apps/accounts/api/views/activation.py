from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from apps.accounts.utils.request_processor import RequestProcessor


class ActivationViewSet(ViewSet):
    permission_classes = [
        IsAuthenticated,
    ]

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def send_mail(self, request):
        processor = RequestProcessor(request, "activation")
        return processor.process_send_activation_request("email")

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def send_sms(self, request):
        processor = RequestProcessor(request, "activation")
        return processor.process_send_activation_request("sms")

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def activate_email(self, request):
        processor = RequestProcessor(request, "activation")
        return processor.process_activation_request("email")

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def activate_phone(self, request):
        processor = RequestProcessor(request, "activation")
        return processor.process_activation_request("phone")
