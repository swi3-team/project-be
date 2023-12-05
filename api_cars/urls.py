from django.urls import path
from .views import *


urlpatterns = [
    # ------------------ BRANDS ------------------
    path("brands", BrandListView.as_view(), name="brands_list"),
    path("brands", BrandAddView.as_view(), name="brand_add"),
    # ------------------ OWNERS ------------------
    path("owners", OwnerListView.as_view(), name="owners_list"),
    path("owners/<int:id>", OwnerDetailView.as_view(), name="owner_detail"),
    path("owners", OwnerAddView.as_view(), name="owner_add"),
    # ------------------ CARS ------------------
    path("", CarListView.as_view(), name="cars_list"),
    path("<int:id>", CarDetailView.as_view(), name="car_detail"),
    path("", CarAddView.as_view(), name="car_add"),
    path("<int:id>", CarEditView.as_view(), name="car_edit"),
    path("<int:id>", CarDeleteView.as_view(), name="car_delete"),
]
