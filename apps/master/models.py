from django.core.cache import cache
from django.db import models

from apps.master.choices import MasterStatusChoices
from apps.users.models import User
from apps.shared.models import BaseModel
from apps.users.choices import GenderChoices


class Master(BaseModel):
    salon = models.ForeignKey(
        'salons.Salons',
        on_delete=models.CASCADE,
        related_name="masters",
        null=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_master")

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    description = models.TextField()
    master_status = models.CharField(choices=MasterStatusChoices.choices)
    gender = models.CharField(choices=GenderChoices.choices)
    languages = models.CharField(max_length=250)
    experiance = models.CharField(max_length=250)
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Master'
        verbose_name_plural = 'Masters'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

