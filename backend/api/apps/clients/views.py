from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Location, Client
from .serializers import ClientSerializer, LocationSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser,]


class LocationViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser,]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
