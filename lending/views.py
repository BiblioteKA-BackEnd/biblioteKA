from django import views
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from follows.permissions import IsAuthenticatedAndNotEmploye
from lending.serializers import LendingSerializer

# Create your views here.


class LendingView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAndNotEmploye]

    serializer_class = LendingSerializer
