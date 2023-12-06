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


class BrandAPIView(APIView):
    def get(self, request):
        brands = Brand.objects.order_by("name")
        serializer = BrandSerializer(brands, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        serializer = BrandAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)


# ------------------ OWNERS ------------------


class OwnerAPIView(APIView):
    def get(self, request):
        owners = Owner.objects.order_by("surname")
        serializer = OwnerSerializer(owners, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        serializer = OwnerAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)


class OwnerDetailView(RetrieveAPIView):
    serializer_class = OwnerDetailSerializer

    def get_object(self):
        if owner_id := self.kwargs.get("id"):
            if owner := Owner.objects.filter(id=owner_id).first():
                return owner
        raise NotFound(detail="Owner not found")


# ------------------ CARS ------------------


class CarAPIView(APIView):
    def get(self, request):
        cars = Car.objects.order_by("year_made")
        serializer = CarListSerializer(cars, many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        serializer = CarAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)


class CarDetailAPIView(APIView):
    def get(self, request, id):
        if car := Car.objects.filter(id=id).first():
            serializer = CarDetailSerializer(car)
            return Response(data=serializer.data, status=200)
        return Response(status=404)

    def put(self, request, id):
        if car := Car.objects.filter(id=id).first():
            serializer = CarEditSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=200)
            return Response(data=serializer.errors, status=400)
        return Response(status=404)

    def delete(self, request, id):
        if car := Car.objects.filter(id=id).first():
            car.delete()
            return Response(status=204)
        return Response(status=404)
