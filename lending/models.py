from django.db import models
from django.utils import timezone

class Lending(models.Model):
    class Meta:
        ordering = ["id"]

    created_at = models.DateTimeField(auto_now_add=True)
    devolution_at = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(hours=48)
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="user_lending"
    )
    copy = models.ForeignKey(
        "books.Copy", on_delete=models.PROTECT, related_name="copy_lending"
    )
