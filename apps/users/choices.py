from django.db import models


class GenderChoices(models.TextChoices):
    MALE = ("erkak", "Erkak")
    AYOL = ("ayol", "Ayol")


class UserStatusChoices(models.TextChoices):
    ADMIN = ("admin", "Admin")
    MASTER = ("master", "Master")
    USER = ("user", "User")
