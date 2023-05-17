from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.models import SocialAccounts


@method_decorator(never_cache, name='dispatch')
class SocialAccountsView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return SocialAccounts.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        from apps.accounts.api.serializers.v1 import SocialAccountsSerializerV1

        if self.request.version == "v1":
            return SocialAccountsSerializerV1
        return SocialAccountsSerializerV1

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        if many:
            for idx, item in enumerate(self.request.data):
                item.update({"user": self.request.user.id})
                self.request.data[idx] = item
        else:
            self.request.data.update(
                    {"user": self.request.user.id})
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=201,
            headers=headers)
