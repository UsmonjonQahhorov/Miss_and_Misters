import random
import re
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import serializers

from config.settings import EMAIL_HOST_USER
from apps.users.models import User, getKey, setKey


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone_number',
            'status'
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone_number',
            'email',
            'password',
            'status',
        ]

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email manzilni kiritishingiz majburiy!")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', value):
            raise serializers.ValidationError("Email manzili @gmail.com bilan tugashi shart.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Ushbu email manzil allaqachon ro'yxatdan o'tgan.")
        return value

    def validate(self, attrs):
        activation_code = random.randint(100000, 999999)
        user = User(
            email=attrs['email'],
            phone_number=attrs['phone_number'],
            password=make_password(attrs['password']),
            is_active=True,
        )
        setKey(
            key=attrs['email'],
            value={
                "user": user,
                "activation_code": activation_code
            },
            timeout=300
        )
        print(getKey(key=attrs['email']))

        send_mail(
            subject="Activation code for your account",
            message=f"Here is your acctivation code: {activation_code}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[attrs['email']],
            fail_silently=False
        )
        return super().validate(attrs)


class CheckActivationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    activation_code = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        email = attrs['email']

        if User.objects.filter(email=email, is_verified=True).exists():
            raise serializers.ValidationError("This email address is already confirmed.")
        else:
            data = getKey(key=attrs['email'])
            if data and 'activation_code' in data and 'user' in data:
                if data['activation_code'] == attrs['activation_code']:
                    user = data['user']
                    user.is_verified = True
                    return attrs

            raise serializers.ValidationError(
                {"error": "Invalid activation code or email"}
            )


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    activation_code = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()


class UserRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            # 'first_name',
            # 'last_name',
            # 'birth_date',
            'email',
            'phone_number',
            # 'gender',
        ]
