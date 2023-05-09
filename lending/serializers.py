import datetime
from rest_framework import serializers
from lending.models import Lending
from datetime import timedelta, datetime
from books.models import Copy

import ipdb


class LendingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        copy = Copy.objects.get(pk=validated_data["copy_id"])

        copy.is_available = False

        copy.save()

        lending_obj = Lending.objects.create(
            **validated_data
        )
        if lending_obj.devolution_at.weekday() in [5, 6]:
            days_extra = 7 - lending_obj.devolution_at.weekday()
            lending_obj.devolution_at += timedelta(days=days_extra)
            lending_obj.save()


        return lending_obj
    
    class Meta:
        model = Lending
        fields = ["user", "copy", "created_at", "devolution_at"]

        read_only_fields = ["user", "copy"]
