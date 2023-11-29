from django.urls import path
from apps.master.views import MasterRegisterCreateAPIView, MasterInfoView

urlpatterns = [
    path("master/api/register", MasterRegisterCreateAPIView.as_view()),
    path('master/api/get-me/', MasterInfoView.as_view())
]
