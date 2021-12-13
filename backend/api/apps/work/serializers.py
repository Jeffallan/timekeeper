from rest_framework import serializers
from .models import WorkPerformed
from api.apps.users.models import Profile, User
from api.apps.services.models import Service
from api.apps.clients.models import Location
from api.apps.users.serializers import IncludeProfileSerializer
from rest_flex_fields import FlexFieldsModelSerializer
from api.apps.clients.serializers import LocationSerializer
from api.apps.users.serializers import UserSerializer
from api.apps.services.serializers import ServiceSerializer
from dry_rest_permissions.generics import DRYPermissionsField



class UserFilter(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        if self.context["request"].user.role == 1:
            return User.objects.all()
        return User.objects.filter(id=self.context["request"].user.id)

class LocationFilter(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        if self.context["request"].user.role == 1:
            return Location.objects.all()
        return Location.objects.filter(providers=self.context["request"].user.id, is_active=True)

class ServiceFilter(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        if self.context["request"].user.role == 1:
            return Service.objects.all()
        return Service.objects.filter(providers=self.context["request"].user.id)


class WorkPerformedSerializer(FlexFieldsModelSerializer):
    provider = UserFilter(default=serializers.CurrentUserDefault(),)
    location = LocationFilter()
    service = ServiceFilter()
    permissions = DRYPermissionsField()
    class Meta:
        model = WorkPerformed
        fields = ["id", "location", "service", "service_date", "start_time",
                  "stop_time", "provider", "billed", "units", "permissions"]
        expandable_fields = {
            "location": (LocationSerializer, ),
            "service": (ServiceSerializer,),
            "provider": (UserSerializer, ),
        }

