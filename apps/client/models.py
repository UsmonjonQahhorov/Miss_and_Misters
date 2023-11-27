from django.db import models
from apps.shared.models import BaseModel
from apps.users.choices import GenderChoices
from apps.users.models import User


class Client(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_client",
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(choices=GenderChoices.choices)
    age = models.IntegerField()
    photo = models.ImageField()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
