from django.db import models


class Book(models.Model):
    class Meta:
        ordering = ["id"]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)


class Copy(models.Model):
    class Meta:
        ordering = ["id"]

    title = models.CharField(max_length=50)
    is_available = models.BooleanField(null=True, default=False)

    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name="copies",
    )
