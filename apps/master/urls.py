from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.master.views import MasterRegisterCreateAPIView
from apps.users.views import (UserRegisterCreateAPIView, UserInfoListAPIView, CheckActivationCodeAPIView,
                              ResetPasswordView, ResetPasswordConfirmView)

urlpatterns = [
    path("master/api/register", MasterRegisterCreateAPIView.as_view()),
    path('master/api/activation', CheckActivationCodeAPIView.as_view()),
]
