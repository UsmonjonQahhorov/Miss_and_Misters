import random
import re
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import serializers
from apps.master.models import Master
from config.settings import EMAIL_HOST_USER
from apps.services.models import Services


class ServiceSerializer(serializers.ModelSerializer):
    class Metaa:
        model = Services
        fields = [
            "category",
            "master",
            "service_name",
            "time_to_took",
            "description",
            "price"
        ]


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"
