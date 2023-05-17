from rest_framework.serializers import ModelSerializer

from apps.accounts.models import * Addresses


class AddressesSerializerV1(ModelSerializer):
    class Meta:
        model = Addresses
        fields = "__all__"
