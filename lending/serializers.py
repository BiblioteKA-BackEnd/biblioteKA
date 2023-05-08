import datetime
from rest_framework import serializers
from lending.models import Lending
from datetime import timedelta, datetime


class LendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ["user_id", "copy_id", "created_at", "devolution_at"]

    def create(self, validated_data):
        lending_obj = Lending.objects.create(
            created_at=datetime.now(),
            devolution_at=datetime.now() + timedelta(hours=48),
        )
        if lending_obj.devolution_at.weekday() in [5, 6]:
            days_extra = 7 - lending_obj.devolution_at.weekday()
            lending_obj.devolution_at += timedelta(days=days_extra)
            lending_obj.save()
        return lending_obj
    

