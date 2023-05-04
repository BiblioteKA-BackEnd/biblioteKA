from django.db import models
from django.utils import timezone

# Create your models here.


class Lending(models.Model):
    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user"
    )
    copy_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    devolution_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=48))