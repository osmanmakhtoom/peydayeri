from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models.profile import Profile


@method_decorator(never_cache, name='dispatch')
class ProfileView(RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_object(self):
        return self.get_queryset()[0]

    def get_serializer_class(self):
        from apps.accounts.api.serializers.v1 import ProfileSerializerV1

        if self.request.version == "v1":
            return ProfileSerializerV1
        return ProfileSerializerV1
