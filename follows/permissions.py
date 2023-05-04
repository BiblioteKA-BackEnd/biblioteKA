from rest_framework import permissions
from users.models import User
from rest_framework.views import Request, View


class IsAuthenticatedAndNotEmploye(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.user.is_authenticated is True
            and request.user.is_employe is False
        )
