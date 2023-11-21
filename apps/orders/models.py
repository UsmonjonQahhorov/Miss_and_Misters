from django.db import models
from apps.users.models import User
from apps.orders.choices import OrderStatusChoice


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    # service_id = models.ForeignKey(Serivice, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    order_price = models.IntegerField()
    order_status = models.CharField(choices=OrderStatusChoice.choices, max_length=255)

from apps.orders.choices import OrderStatusChoice
from apps.users.models import User


class Order(models.Model):
    user_id = models.ManyToOneRel(
        User,
        related_name="user"
    )
    # service_id = models.ForeignKey(Serivice, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    order_price = models.IntegerField()
    order_status = models.CharField(choices=OrderStatusChoice.choices)


    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
         return str(self.order_date)
        

