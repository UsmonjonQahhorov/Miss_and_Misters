from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

from apps.users.choices import GenderChoices, UserStatusChoices
from apps.users.manager import UserManager
from apps.users.validators import CustomEmailValidator


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(validators=[CustomEmailValidator()])
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    password = models.CharField(max_length=250)
    status = models.CharField(choices=UserStatusChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        return f"{self.username}"


def getKey(key):
    return cache.get(key)


def setKey(key, value, timeout):
    cache.set(key, value, timeout)
