from rest_framework import serializers
from ..models import *
from .brand import BrandSerializer
from .owner import OwnerSerializer


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "type",
            "image_url",
        )


class CarDetailSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "type",
            "country",
            "year_made",
            "engine",
            "image_url",
            "brand",
            "owner",
        )

    def get_brand(self, obj):
        return BrandSerializer(obj.brand).data

    def get_owner(self, obj):
        return OwnerSerializer(obj.owner).data


class CarAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            "name",
            "type",
            "country",
            "year_made",
            "engine",
            "image_url",
            "brand",
            "owner",
        )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)


class CarEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("owner",)

    def update(self, instance, validated_data):
        instance.owner = validated_data.get("owner", instance.owner)
        instance.save()
        return instance


class CarDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ()