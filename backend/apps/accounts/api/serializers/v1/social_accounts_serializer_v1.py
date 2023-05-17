from rest_framework.serializers import ModelSerializer

from apps.accounts.models import SocialAccounts


class SocialAccountsSerializerV1(ModelSerializer):
    class Meta:
        model = SocialAccounts
        fields = '__all__'
