from rest_framework import permissions
from users.models import User
from rest_framework.views import Request, View


class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_employe
        )


class IsEmployeeOrUserOwner(permissions.BasePermission):
    def has_object_permission(
            self, request: Request, view: View, obj: User
    ) -> bool:
        if request.user.is_authenticated:
            return (
                request.user.is_employe or obj == request.user
            )


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated
