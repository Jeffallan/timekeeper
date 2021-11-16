from rest_framework import serializers
from .models import Client, Location
from api.apps.users.serializers import IncludeProfileSerializer



class IncludeClientSerializer(serializers.ModelSerializer):
    class Meta:

        model = Client
        fields = ["id", "name", "address_1", "address_2", "created", "updated",
                  "city", "state", "zip_code", "phone_number", "mailing_address",]


class LocationSerializer(serializers.ModelSerializer):

    provider_details = IncludeProfileSerializer(read_only=True, many=True)
    client = IncludeClientSerializer(read_only=True)

    class Meta:
        model = Location
        #depth = 2
        fields = ["id", "name", "client", "address_1", "address_2", "created", "updated",
                  "city", "state", "zip_code", "phone_number", "mailing_address", "providers", "provider_details"]


class ClientSerializer(serializers.ModelSerializer):

    locations = serializers.SerializerMethodField()

    def get_locations(self, obj):
        qs = Location.objects.filter(client__id=obj.id)
        return LocationSerializer(qs, many=True, context=self.context).data

    class Meta:
        model = Client
        fields = ["id", "name", "address_1", "address_2", "created", "updated",
                  "city", "state", "zip_code", "phone_number", "mailing_address", "locations"]