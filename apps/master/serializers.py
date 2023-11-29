import random
import re

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import serializers

from apps.master.models import Master
from apps.users.models import getKey, setKey, User
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


class MasterRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30, write_only=True)
    last_name = serializers.CharField(max_length=30, write_only=True)
    description = serializers.CharField(max_length=250, write_only=True)
    master_status = serializers.CharField(write_only=True)
    language = serializers.CharField(max_length=30, write_only=True)
    experiance = serializers.CharField(max_length=20, write_only=True)
    gender = serializers.CharField(write_only=True)
    age = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=15, write_only=True)
    email = serializers.EmailField(max_length=30, write_only=True)
    password = serializers.CharField(max_length=150, write_only=True)

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email manzilni kiritishingiz kerak.")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', value):
            raise serializers.ValidationError("Email manzilni @gmail.com bilan tugatish kerak.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Ushbu email manzil allaqachon ro'yxatdan o'tgan.")
        return value

    def validate(self, attrs):
        print(f"attrs: {attrs}")
        activation_code = random.randint(100000, 999999)
        user = User(
            email=attrs['email'],
            phone_number=attrs['phone_number'],
            password=make_password(attrs['password']),
            is_active=True,
            status="master",
        )
        user.save()

        master = Master(
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
            master_status=attrs['master_status'],
            description=attrs['description'],
            gender=attrs['gender'],
            languages=attrs['language'],
            experiance=attrs['experiance'],
            age=attrs['age'],
            user=user
        )
        master.save()

        setKey(
            key=attrs['email'],
            value={
                "user": user,
                "master": master,
                "activation_code": activation_code
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
        return attrs


class MasterRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = [
            'first_name',
            'last_name',
            'description',
            'languages',
            'salon_id',
            'experiance',
            'age',
        ]
