from rest_framework import permissions
from users.models import User
from lending.models import Lending
from rest_framework.views import Request, View


class IsEmployeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_employe
        )


class IsEmployeOrUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated:
            return request.user.is_employe or obj == request.user


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return obj == request.user


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated
