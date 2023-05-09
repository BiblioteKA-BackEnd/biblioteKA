from django import views
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from lending.models import Lending
from lending.serializers import LendingSerializer
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsEmployeOrReadOnly

from books.models import Book

import ipdb

# Create your views here.


class LendingView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = LendingSerializer


class LendingDetailView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeOrReadOnly]

    queryset = Lending.objects.all()
    serializer_class = LendingSerializer

    def perform_create(self, serializer):
        
        book_id = self.kwargs.get("pk_book")

        book = Book.objects.get(pk=book_id)

        copy_book = 0


        for i in book.copies.all():
            if i.is_available:
                copy_book = i.id

                break
        

        return serializer.save(user_id=self.request.user.id, copy_id=copy_book)
