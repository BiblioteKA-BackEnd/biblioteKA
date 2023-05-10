from rest_framework import permissions
from users.models import User
from lending.models import Lending
from rest_framework.views import Request, View
from django.utils import timezone
import ipdb


class IsUserLate(permissions.BasePermission):
    message = "Users with pending deliveries cannot take out new loans"

    def has_permission(self, request: Request, view: View):
        user = User.objects.get(pk=view.kwargs.get("pk_user"))
        lendings = Lending.objects.filter(user_id=view.kwargs.get("pk_user"))
        for lending in lendings.all():
            if lending.devolution_at < timezone.now():
                user.is_late = True
                user.save()
        if user.is_late:
            return False
        return True
