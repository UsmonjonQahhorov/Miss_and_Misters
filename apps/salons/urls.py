from django.urls import path

from apps.salons.views import SalonsDetailViewSet, SalonsUpdateViewSet, SalonsDeleteViewSet, \
    SalonsCreateViewSet

urlpatterns = [
    path('salon/create/', SalonsCreateViewSet.as_view()),
    path('salon/detail/<int:pk>/', SalonsDetailViewSet.as_view()),
    path('salon/update/<int:pk>/', SalonsUpdateViewSet.as_view()),
    path('salon/delete/<int:pk>/', SalonsDeleteViewSet.as_view())
]
