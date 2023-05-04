from rest_framework import serializers
from .models import Book, Copy


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "id", "title", "author", "copies"
        read_only_fields = ["copies", "id"]


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = "id", "title", "is_available", "book"
        read_only_fields = ["book", "id"]
