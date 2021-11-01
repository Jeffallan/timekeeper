from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        return obj == request.user

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 1


class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 2

class IsUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 3