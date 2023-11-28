import random
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response

from apps.master.models import Master
from apps.users.models import User, getKey
from apps.users.permissions import UserPermission
from apps.users.serializers import UserRegisterSerializer, UserRetriveSerializer, CheckActivationCodeSerializer, \
    ResetPasswordConfirmSerializer, ResetPasswordSerializer


class UserRegisterCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProfileInfoListAPIView(ListAPIView):
    permission_classes = [UserPermission]
    serializer_class = UserRetriveSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return User.objects.all()
            elif hasattr(user, 'master'):
                return Master.objects.filter(user_ptr=user.id)
            else:
                return User.objects.filter(id=user.id)
        else:
            return User.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CheckActivationCodeAPIView(GenericAPIView):
    serializer_class = CheckActivationCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = getKey(key=data['email'])['user']
        user.is_verified = True
        user.is_active = True
        user.save()
        return Response({"message": "Your email has been confirmed"}, status=status.HTTP_200_OK)


class ResetPasswordView(CreateAPIView):
    serializer_class = ResetPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "User not found with this email."}, status=status.HTTP_400_BAD_REQUEST)

            activation_code = str(random.randint(100000, 999999))
            user.set_password(activation_code)
            user.save()

            send_mail(
                'Password Reset Confirmation',
                f'Your password reset code is: {activation_code}',
                'admin@example.com',
                [email],
                fail_silently=False,
            )

            return Response({"detail": "Password reset code sent to your email."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordConfirmView(CreateAPIView):
    serializer_class = ResetPasswordConfirmSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            activation_code = serializer.validated_data['activation_code']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"detail": "User not found with this email."}, status=status.HTTP_400_BAD_REQUEST)

            if user.check_password(activation_code):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return Response({"detail": "Password reset successfully."}, status=status.HTTP_200_OK)
                else:
                    return Response({"detail": "New password and confirm password do not match."},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "Invalid activation code."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
