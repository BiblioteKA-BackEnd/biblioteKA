from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"
