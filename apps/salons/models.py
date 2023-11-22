from django.db import models
from apps.shared.models import BaseModel
from apps.region_districts.models import District, Region


class Salons(BaseModel):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="regions"
    )

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        related_name='districts'
    )

    name = models.CharField(max_length=255)
    opening_time = models.CharField(max_length=5)
    closing_time = models.CharField(max_length=5)
    address_line = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Salon"
        verbose_name_plural = "Salons"

    def __str__(self):
        return f"{self.name}"
