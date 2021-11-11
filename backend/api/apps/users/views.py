from rest_framework.response import Response
from rest_framework import serializers, status, viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action, permission_classes
from .models import Profile, User
from api.apps.core.permissions import IsAdmin
from .serializers import CreateUserSerializer, UserSerializer, AdminUserSerializer, ProfileSerializer, AdminProfileSerializer
from dry_rest_permissions.generics import DRYPermissions
from rest_framework import mixins


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser,]


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    #serializer_class = ProfileSerializer
    permission_classes = (DRYPermissions,)

    def get_serializer_class(self):
        if self.request.user.role == 1:
            return AdminProfileSerializer
        return ProfileSerializer