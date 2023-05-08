from rest_framework import permissions
from users.models import User
from rest_framework.views import Request, View


class IsAuthenticatedAndNotEmploye(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.user.is_authenticated
            and not request.user.is_employe
        )


class IsEmailAlredyRegister(permissions.BasePermission):
    message = "email alredy register"

    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.email:
            if User.objects.filter(email=obj.email):
                return False
