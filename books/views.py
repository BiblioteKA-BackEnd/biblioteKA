from books.models import Book
from books.serializers import BookSerializer
from users.permissions import IsEmployeOrUserOwner, IsEmployeOrReadOnly
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeOrReadOnly]

    serializer_class = BookSerializer


class BookDetailedView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeOrUserOwner]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"
