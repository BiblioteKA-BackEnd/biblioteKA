from rest_framework import serializers
from follows.models import Follow
from users.models import User
from books.models import Book
from django.core.mail import send_mail
from django.conf import settings


class FollowSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Follow:
        user = User.objects.get(id=validated_data["user_id"])
        book = Book.objects.get(id=validated_data["book_id"])
        send_mail(
            subject=user.username,
            message=f"You are following {book.title}, you will receive a notice whenever it becomes available",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[validated_data["email"]],
            fail_silently=False
        )
        return Follow.objects.create(**validated_data)

    def update(self, instance: Follow, validated_data: dict) -> Follow:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Follow
        fields = [
            "email",
            "user_id",
            "book_id",
        ]
        read_only_fields = ["user_id", "book_id"]
