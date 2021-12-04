from rest_framework import viewsets
from .models import WorkPerformed
from .serializers import WorkPerformedSerializer
from api.apps.users.models import User
from dry_rest_permissions.generics import DRYPermissions


class WorkPerformedViewSet(viewsets.ModelViewSet):
    queryset = WorkPerformed.objects.all()
    serializer_class = WorkPerformedSerializer
    permission_classes = [DRYPermissions,]

    def get_queryset(self):
        if self.request.user.role == 1:
            return WorkPerformed.objects.all()
        return WorkPerformed.objects.filter(provider=self.request.user.id)
