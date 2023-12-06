from rest_framework.exceptions import NotFound
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.generics import ListAPIView
from .models import *
from .serializers import *


# ------------------ BRANDS ------------------


class BrandListView(ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brand.objects.order_by("name")


class BrandAddView(CreateAPIView):
    serializer_class = BrandAddSerializer

    def post(self, request, *args, **kwargs):
        serializer = BrandAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)


# ------------------ OWNERS ------------------


class OwnerListView(ListAPIView):
    serializer_class = OwnerSerializer

    def get_queryset(self):
        return Owner.objects.order_by("surname")


class OwnerDetailView(RetrieveAPIView):
    serializer_class = OwnerDetailSerializer

    def get_object(self):
        if owner_id := self.kwargs.get("id"):
            if owner := Owner.objects.filter(id=owner_id).first():
                return owner
        raise NotFound(detail="Owner not found")


class OwnerAddView(CreateAPIView):
    serializer_class = OwnerAddSerializer

    def post(self, request, *args, **kwargs):
        serializer = OwnerAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)


# ------------------ CARS ------------------


class CarListView(ListAPIView):
    serializer_class = CarListSerializer

    def get_queryset(self):
        return Car.objects.order_by("year_made")


class CarDetailView(RetrieveAPIView):
    serializer_class = CarDetailSerializer

    def get_object(self):
        if car_id := self.kwargs.get("id"):
            if car := Car.objects.filter(id=car_id).first():
                return car
        raise NotFound(detail="Car not found")


class CarAddView(CreateAPIView):
    serializer_class = CarAddSerializer


class CarEditView(UpdateAPIView):
    serializer_class = CarEditSerializer

    def get_object(self):
        if car_id := self.kwargs.get("id"):
            if car := Car.objects.filter(id=car_id).first():
                return car
        raise NotFound(detail="Car not found")


class CarDeleteView(DestroyAPIView):
    serializer_class = CarDeleteSerializer

    def get_object(self):
        if car_id := self.kwargs.get("id"):
            if car := Car.objects.filter(id=car_id).first():
                return car
        raise NotFound(detail="Car not found")

    def delete(self, request, *args, **kwargs):
        car = self.get_object()
        car.delete()
        return Response(status=204)
