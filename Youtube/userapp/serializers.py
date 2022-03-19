from rest_framework.serializers import ModelSerializer

from .models import *


class AccountSerializers(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'