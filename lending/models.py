from pyexpat import model
from django.db import models


class Lending(models.Model):
    copy_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    devolution_at = models.DateTimeField()
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user"
    )
