from books.models import Book
from books.serializers import BookSerializer
from users.permissions import (
    IsEmployeOrUserOwner,
    IsEmployeOrReadOnly,
    IsAuthenticated
)
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailedView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeOrUserOwner]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"
