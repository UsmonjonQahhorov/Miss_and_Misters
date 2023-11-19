from django.db import models


class OrderStatusChoice(models.TextChoices):
    NEW = ("yangi", "YANGI")
    WAIT = ("kutmoqda", "KUTMOQDA")
    STOPPED = ("toxtatildi", "TOXTATILDI")
    FINISHED = ("yakunlandi", "YAKUNLANDI")
