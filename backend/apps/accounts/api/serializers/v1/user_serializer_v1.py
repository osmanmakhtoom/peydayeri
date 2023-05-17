from rest_framework.serializers import ModelSerializer

from apps.accounts.models.user import User


class UserSerializerV1(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            "password":
            {
                "write_only": True
            }
        }
