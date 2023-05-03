from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        max_length=120,
        unique=True
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_employe = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # follow = models.ForeignKey(
    #   "follow.Follow",
    #   on_delete=models.CASCADE,
    #   related_name="follow"
    # )