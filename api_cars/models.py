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
