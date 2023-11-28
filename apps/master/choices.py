from django.db import models


class MasterStatusChoices(models.TextChoices):
    ACTIVE = ("active", "ACTIVE")
    PASSIVE = ("passive", "PASSIVE")
