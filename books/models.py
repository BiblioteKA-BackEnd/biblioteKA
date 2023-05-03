from django.db import models


class Book(models.Model):
    class Meta:
        ordering = ["id"]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    follow = models.ForeignKey(
        "follows.Follow",
        on_delete=models.CASCADE,
        related_name="books",
    )


class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    title = models.CharField(max_length=50)
    is_available = models.BooleanField()

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="copies",
    )
