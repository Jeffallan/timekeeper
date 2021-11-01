from rest_framework.response import Response
from rest_framework import serializers, status, viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action, permission_classes
from .models import User
from api.apps.core.permissions import IsAdmin
from .serializers import CreateUserSerializer, UserSerializer, AdminUserSerializer



class UserViewSet(
                  viewsets.ModelViewSet
                 ):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser,]

