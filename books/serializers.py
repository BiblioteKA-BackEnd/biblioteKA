from rest_framework import serializers
from .models import Book, Copy


class CopySerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    title = serializers.CharField(source="book.title", read_only=True)

    class Meta:
        model = Copy
        fields = "id", "title", "is_available", "book"
        read_only_fields = ["book", "id"]


class BookSerializer(serializers.ModelSerializer):
    copies = CopySerializer(many=True, read_only=True)

    def create(self, validated_data: dict) -> Book:
        copy = validated_data.pop("copy")
        created_book = Book.objects.create(**validated_data)
        for i in range(copy):
            Copy.objects.create(book=created_book)
        return created_book

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = "id", "title", "author", "copies", "copy"
        read_only_fields = ["copies", "id"]
        extra_kwargs = {"copy": {"write_only": True}}
