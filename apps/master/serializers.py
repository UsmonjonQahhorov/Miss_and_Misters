import random
import re

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import status
from rest_framework import serializers
from apps.master.models import Master, setKey, getKey
from config.settings import EMAIL_HOST_USER


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = [
            'first_name',
            'last_name',
            'description',
            'status',
            'gender',
            'languages',
            'experiance',
            'age'
        ]


class MasterRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = [
            'first_name',
            'last_name',
            'description',
            'email',
            'phone_number',
            'status',
            'gender',
            'languages',
            'experiance',
            'age',
            'password',
        ]

    def validate(self, value):
        if not value:
            raise serializers.ValidationError("Email manzilni kiritish majburiy. ")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', value):
            raise serializers.ValidationError("Email manzili @gmail.com bilan tugashi kerak. ")
        if Master.objects.filter(email=value).exists():
            raise serializers.ValidationError("Ushbu email bilan allaqachon ro'yxatdan o'tilgan. ")
        return value

    def validate(self, attrs):
        activation_code = random.randint(100000, 999999)
        master = Master(
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
            email=attrs['email'],
            phone_number=attrs['phone_number'],
            description=attrs['description'],
            gender=attrs['gender'],
            languages=attrs['languages'],
            experiance=attrs['experiance'],
            age=attrs['age'],
            password=make_password(attrs['password']),
        )
        setKey(
            key=attrs['email'],
            value={
                "user": master,
                "activate_code": activation_code
            },
            timeout=300
        )
        print(getKey(key=attrs['email']))
        send_mail(
            subject="Activation code for your account",
            message=f"Your activate code.\n{activation_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[attrs['email']],
            fail_silently=False,
        )
        return super().validate(attrs)
