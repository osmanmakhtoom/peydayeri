from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models.user import User


@method_decorator(never_cache, name='dispatch')
class UserView(RetrieveAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        from apps.accounts.api.serializers.v1 import UserSerializerV1
        if self.request.version == "v1":
            return UserSerializerV1
        return UserSerializerV1
