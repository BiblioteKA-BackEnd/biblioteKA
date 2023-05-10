from django import views
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from lending.models import Lending
from lending.serializers import LendingSerializer

from users.permissions import IsEmployeOrReadOnly, IsAuthenticated
from lending.permissions import IsUserLate

from books.models import Book
from users.models import User

from django.utils import timezone


class LendingDetailViewCreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeOrReadOnly, IsUserLate]

    queryset = Lending.objects.all()
    serializer_class = LendingSerializer
    lookup_url_kwarg = "pk_user"

    def perform_create(self, serializer):
        book_id = self.kwargs.get("pk_book")
        book = Book.objects.get(pk=book_id)
        copy_book = 0

        for i in book.copies.all():
            if i.is_available:
                copy_book = i.id

                break

        return serializer.save(
            user_id=self.kwargs.get("pk_user"),
            copy_id=copy_book
        )


class LendingDetailViewList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeOrReadOnly]

    queryset = Lending.objects.all()
    serializer_class = LendingSerializer
    lookup_url_kwarg = "pk_user"

    def get_queryset(self):
        users = Lending.objects.filter(user_id=self.kwargs.get("pk_user"))

        return users


class LendingDetailViewDestroy(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeOrReadOnly]

    queryset = Lending.objects.all()
    serializer_class = LendingSerializer
    lookup_url_kwarg = "pk_lending"

    def perform_destroy(self, instance):
        print(instance)
        user = User.objects.get(pk=instance.user_id)
        lendings = Lending.objects.filter(user_id=instance.user_id)
        for lending in lendings.all():
            if lending.devolution_at > timezone.now():
                user.is_late = False
                user.save()
        instance.delete()
        return True
