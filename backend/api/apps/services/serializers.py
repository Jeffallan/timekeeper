from rest_framework import serializers
from .models import Service
from api.apps.users.serializers import UserSerializer
from rest_flex_fields import FlexFieldsModelSerializer


class ServiceSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name", "service_unit", "is_duration", "created", "updated", "providers"]
        expandable_fields = {
            "providers": (UserSerializer, {"many": True, "read_only": True})
        }