from django.db import models
from apps.shared.models import BaseModel


class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.name
