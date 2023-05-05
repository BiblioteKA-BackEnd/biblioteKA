from follows.models import Follow
from follows.serializers import FollowSerializer
from follows.permissions import IsAuthenticatedAndNotEmploye
from users.permissions import IsAuthenticated, IsEmployeOrUserOwner
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class FollowView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAndNotEmploye]

    serializer_class = FollowSerializer
    lookup_url_kwarg = "pk_book"

    def perform_create(self, serializer):
        return serializer.save(
            email=self.request.user.email,
            user_id=self.request.user.id,
            book_id=self.kwargs.get("pk_book")
        )


class FollowDetailedView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsEmployeOrUserOwner]

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    lookup_url_kwarg = "pk_follow"
