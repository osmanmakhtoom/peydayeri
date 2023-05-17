from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Profile


class ProfileSerializerV1(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "is_phone_activated": {"read_only": True},
            "is_email_activated": {"read_only": True},
            "user": {"read_only": True},
        }
