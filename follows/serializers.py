from rest_framework import serializers
from follows.models import Follow


class FollowSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Follow:
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
