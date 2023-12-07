from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = "brands"
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return f"Car brand: {self.name} from {self.country}"


class Owner(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = "owners"
        verbose_name = _("Owner")
        verbose_name_plural = _("Owners")

    def __str__(self):
        return f"Owner: {self.name} {self.surname}\nCity: {self.city}\nAge: {self.age}\nGender: {self.gender}"


class Car(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    year_made = models.PositiveBigIntegerField()
    type = models.CharField(max_length=100, null=False, blank=False)
    engine = models.CharField(max_length=100, null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)

    class Meta:
        db_table = "cars"
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    def __str__(self):
        return f"Car with name: {self.name} from company: {self.country}, this car is of type: {self.type}"
