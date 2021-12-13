from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Location, Client
from .serializers import ClientSerializer, LocationSerializer
from dry_rest_permissions.generics import DRYPermissions


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser,]


class LocationViewSet(viewsets.ModelViewSet):

    permission_classes = [DRYPermissions,]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def get_queryset(self):
        if self.request.user.role == 1:
            return Location.objects.all()
        return Location.objects.filter(providers__in=[self.request.user.id])
