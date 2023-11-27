from django.db import models
from apps.shared.models import BaseModel


class Services(BaseModel):
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="service_category"
    )

    master = models.ForeignKey(
        "master.Master",
        on_delete=models.CASCADE,
        related_name="masters_services"
    )

    service_name = models.CharField(max_length=250)
    time_to_took = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f"{self.service_name}"


class Category(BaseModel):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"
