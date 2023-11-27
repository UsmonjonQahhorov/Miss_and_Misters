from django.db import models

from apps.client.models import Client
from apps.master.models import Master
from apps.users.models import User
from apps.orders.choices import OrderStatusChoice


class Order(models.Model):
    master = models.ForeignKey(
        Master,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="masters_order"
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="client_orders"
    )

    service = models.ForeignKey(
        "services.Services",
        on_delete=models.PROTECT,
        related_name="service_orders"
    )
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices=OrderStatusChoice.choices, max_length=255)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return str(self.order_date)
