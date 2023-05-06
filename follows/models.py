from django.db import models


class Follow(models.Model):
    class Meta:
        ordering = ["id"]

    email = models.EmailField(max_length=120, blank=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="user_follows"
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.PROTECT,
        related_name="book_follows"
    )
