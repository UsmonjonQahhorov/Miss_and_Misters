import random
import re

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import status
from rest_framework import serializers
from apps.master.models import Master, getCash, setKeyword
from apps.users.models import getKey

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

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError("Email manzilni kiritish majburiy. ")
        email = attrs['email']
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email):
            raise serializers.ValidationError("Email manzili @gmail.com bilan tugashi kerak. ")
        if Master.objects.filter(email=email).exists():
            raise serializers.ValidationError("Ushbu email bilan allaqachon ro'yxatdan o'tilgan. ")

        activation_code = random.randint(100000, 999999)
        master = Master(
            first_name=attrs['first_name'],
            last_name=attrs['last_name'],
            email=email,
            phone_number=attrs['phone_number'],
            description=attrs['description'],
            gender=attrs['gender'],
            languages=attrs['languages'],
            experiance=attrs['experiance'],
            age=attrs['age'],
            password=make_password(attrs['password']),
        )
        setKeyword(
            key=email,
            value={
                "master": master,
                "activation_code": activation_code
            },
            timeout=300
        )

        print(getCash(key=attrs['email']))
        send_mail(
            subject="Activation code for your account",
            message=f"Your activate code.\n{activation_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        return attrs


class CheckMActivationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    activation_code = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        email = attrs['email']
        if Master.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email address is already confirmed.")
        else:
            data = getKey(key=email)
            print(f"data: {data}")
            if data and 'activation_code' in data and 'master' in data:
                if data['activation_code'] == attrs['activation_code']:
                    master = data['master']
                    master.is_verified = True
                    master.save()
                    return attrs

            raise serializers.ValidationError(
                {"error": "Invalid activation code or email"}
            )
