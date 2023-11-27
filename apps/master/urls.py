from django.urls import path
from apps.master.views import MasterRegisterCreateAPIView, CheckActivationCodeAPIView, MasterInfoView

urlpatterns = [
    path("master/api/register", MasterRegisterCreateAPIView.as_view()),
    path('master/api/activation', CheckActivationCodeAPIView.as_view()),
    path('master/api/get-me/', MasterInfoView.as_view())
]
