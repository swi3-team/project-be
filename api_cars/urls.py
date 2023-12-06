from django.urls import path
from .views import *


urlpatterns = [
    # ------------------ BRANDS ------------------
    path("brands", BrandAPIView.as_view(), name="brands_list_add"),
    # ------------------ OWNERS ------------------
    path("owners", OwnerAPIView.as_view(), name="owners_list_add"),
    path("owners/<int:id>", OwnerDetailView.as_view(), name="owner_detail"),
    # ------------------ CARS ------------------
    path("", CarAPIView.as_view(), name="cars_list_add"),
    path("<int:id>", CarDetailAPIView.as_view(), name="car_detail_update_delete"),
]
