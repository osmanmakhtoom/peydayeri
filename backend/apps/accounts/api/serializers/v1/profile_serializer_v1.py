from rest_framework.serializers import ModelSerializer

from apps.accounts.models import Profile


class ProfileSerializerV1(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "is_phone_activated",
            "is_email_activated",
            "user",
        ]
