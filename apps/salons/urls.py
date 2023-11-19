from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.salons.views import SalonsDetailViewSet, SalonsUpdateViewSet, SalonsDeleteViewSet, \
    SalonsCreateViewSet

router = DefaultRouter()

urlpatterns = [
                  path('create/', SalonsCreateViewSet.as_view(),
                       name='salons-create'),
                  path('detail/<int:pk>/', SalonsDetailViewSet.as_view(),
                       name='salons-detail'),
                  path('update/<int:pk>/', SalonsUpdateViewSet.as_view(),
                       name='salons-update'),
                  path('delete/<int:pk>/', SalonsDeleteViewSet.as_view(),
                       name='salons-delete')
              ] + router.urls
