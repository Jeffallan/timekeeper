from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Service
from .serializers import ServiceSerializer
from dry_rest_permissions.generics import DRYPermissions


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [DRYPermissions,]

    def get_queryset(self):
        if self.request.user.role == 1:
            return Service.objects.all()
        return Service.objects.filter(approved_providers__in=[self.request.user.id])
