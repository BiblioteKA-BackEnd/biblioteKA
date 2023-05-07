from django.db import models
from django.utils import timezone

class Lending(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    devolution_at = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(hours=48)
    )

    user_id = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="user_lending"
    )
    copy_id = models.ForeignKey(
        "books.Copy", on_delete=models.PROTECT, related_name="copy_lending"
    )
