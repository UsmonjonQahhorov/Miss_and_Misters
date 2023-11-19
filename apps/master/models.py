from django.db import models
from django.core.cache import cache
from apps.shared.models import BaseModel
from apps.users.choices import GenderChoices


class Master(BaseModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField(default=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(choices=GenderChoices.choices)
    languages = models.CharField(max_length=250)
    experiance = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    age = models.IntegerField()

    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Master'
        verbose_name_plural = 'Masters'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def getCash(key):
    return cache.get(key)


def setKeyword(key, value, timeout):
    cache.set(key, value, timeout)
