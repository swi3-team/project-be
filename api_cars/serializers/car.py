from rest_framework import serializers
from ..models import *
from .brand import BrandSerializer
from .owner import OwnerSerializer


class CarListSerializer(serializers.ModelSerializer):
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
        return BrandSerializer(obj.brand_id).data

    def get_owner(self, obj):
        return OwnerSerializer(obj.owner_id).data


class CarDetailSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

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

    def get_brand(self, obj):
        return BrandSerializer(obj.brand_id).data

    def get_owner(self, obj):
        return OwnerSerializer(obj.owner_id).data


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
            "brand_id",
            "owner_id",
        )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)


class CarEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.Name = validated_data.get("Name", instance.name)
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance


class CarDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ()
