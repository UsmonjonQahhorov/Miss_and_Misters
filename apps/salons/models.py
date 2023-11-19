from django.db import models

from apps.shared.models import BaseModel


class Salons(BaseModel):
    name = models.CharField(max_length=255)
    opening_time = models.CharField(max_length=5)
    closing_time = models.CharField(max_length=5)
    address_line = models.CharField(max_length=255)

    class Meta:
        verbose_name = "salon"
        verbose_name_plural = "salons"

    def __str__(self):
        return f"{self.name}"
