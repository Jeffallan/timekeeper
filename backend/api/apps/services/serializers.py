from rest_framework import serializers
from .models import Service
from api.apps.users.serializers import AdminUserSerializer
from rest_flex_fields import FlexFieldsModelSerializer


class ServiceSerializer(FlexFieldsModelSerializer):
    #approved_providers = IncludeProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = ["name", "service_unit", "is_duration", "created", "updated", "approved_providers"]
        expandable_fields = {
            "approved_providers": (AdminUserSerializer, {"many": True, "read_only": True})
        }