from rest_framework import serializers
from ..models import *


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"


class OwnerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"


class OwnerAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = (
            "name",
            "surname",
            "city",
            "age",
            "gender",
        )

    def create(self, validated_data):
        return Owner.objects.create(**validated_data)
