from rest_framework import serializers

from lending.models import Lending


class LendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ["user_id", "copy_id", "created_at", "devolution_at"]
