from rest_framework import serializers
from .models import Service
from api.apps.users.serializers import IncludeProfileSerializer


class ServiceSerializer(serializers.ModelSerializer):
    approved_providers = IncludeProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = "__all__"