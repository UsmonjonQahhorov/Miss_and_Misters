from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.views import (UserRegisterCreateAPIView, UserInfoListAPIView, CheckActivationCodeAPIView,
                              ResetPasswordView, ResetPasswordConfirmView)

urlpatterns = [
    path('user/api/get-me', UserInfoListAPIView.as_view()),
    path('user/api/register', UserRegisterCreateAPIView.as_view()),
    path('user/api/check-activation-code', CheckActivationCodeAPIView.as_view()),
    path('user/api/reset-password', ResetPasswordView.as_view()),
    path('user/api/reset-conifirm', ResetPasswordConfirmView.as_view()),
    path('user/api/login', TokenObtainPairView.as_view()),
]
