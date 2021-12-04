from rest_framework import serializers
from .models import Client, Location
from api.apps.users.serializers import AdminUserSerializer
from rest_flex_fields import FlexFieldsModelSerializer



class IncludeClientSerializer(serializers.ModelSerializer):
    class Meta:

        model = Client
        fields = ["id", "name", "address_1", "address_2", "created", "updated",
                  "city", "state", "zip_code", "phone_number", "mailing_address", "is_active"]


class LocationSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Location
        fields = ["id", "name", "client", "address_1", "address_2", "created", "updated",
                  "city", "state", "zip_code", "phone_number", "mailing_address",  "providers", "is_active"]
        expandable_fields = {
            "providers": (AdminUserSerializer, {"many": True}),
            "client": (IncludeClientSerializer, )
        }


class ClientSerializer(serializers.ModelSerializer):

    locations = serializers.SerializerMethodField()

    def get_locations(self, obj):
        qs = Location.objects.filter(client__id=obj.id).prefetch_related()
        return LocationSerializer(qs, many=True, context=self.context).data

    class Meta:
        model = Client
        depth = 3
        fields = ["id", "name", "address_1", "address_2", "created", "updated",
                  "city", "state", "zip_code", "phone_number", "mailing_address", "locations", "is_active"]
        expandable_fields = {
            "locations": (LocationSerializer),
        }