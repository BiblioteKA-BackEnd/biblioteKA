from django.db import models


class Follow(models.Model):
    email = models.EmailField(max_length=120)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="user_book_follows"
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.PROTECT,
        related_name="book_follows"
    )
