from rest_framework import serializers
from ..models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class BrandAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "name",
            "country",
        )

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)
