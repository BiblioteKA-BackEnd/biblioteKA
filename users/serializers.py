from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        for key in validated_data.items():
            if key == "is_employe":
                return User.objects.create_superuser(**validated_data)
        
        return User.objects.create_user(**validated_data)
    
    email = serializers.EmailField(
        validators=[UniqueValidator(
                    queryset=User.objects.all(),
                    message="This field must be unique.")],
    )
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_employe",
            "is_late",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}