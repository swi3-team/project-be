from django.urls import path
from .views import *


urlpatterns = [
    # ------------------ BRANDS ------------------
    path("brands/all", BrandListView.as_view(), name="brands_list"),
    path("brands/add/", BrandAddView.as_view(), name="brand_add"),
    # ------------------ OWNERS ------------------
    path("owners/all", OwnerListView.as_view(), name="owners_list"),
    path("owners/<int:id>/", OwnerDetailView.as_view(), name="owner_detail"),
    path("owners/add/", OwnerAddView.as_view(), name="owner_add"),
    # ------------------ CARS ------------------
    path("all", CarListView.as_view(), name="cars_list"),
    path("<int:id>/", CarDetailView.as_view(), name="car_detail"),
    path("add/", CarAddView.as_view(), name="car_add"),
    path("edit/<int:id>/", CarEditView.as_view(), name="car_edit"),
    path("delete/<int:id>/", CarDeleteView.as_view(), name="car_delete"),
]
