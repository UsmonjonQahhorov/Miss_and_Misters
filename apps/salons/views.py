from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from apps.salons.models import Salons
from apps.salons.serializers import SalonsSerializer, SalonsCreateSerializer
from apps.users.permissions import UserPermission


class SalonsCreateViewSet(CreateAPIView):
    queryset = Salons.objects.all()
    serializer_class = SalonsCreateSerializer
    permission_classes = [UserPermission]


class SalonsDeleteViewSet(DestroyAPIView):
    queryset = Salons.objects.all()
    serializer_class = SalonsSerializer
    permission_classes = [UserPermission]


class SalonsUpdateViewSet(UpdateAPIView):
    queryset = Salons.objects.all()
    serializer_class = SalonsCreateSerializer
    permission_classes = [UserPermission]


class SalonsDetailViewSet(RetrieveAPIView):
    queryset = Salons.objects.all()
    serializer_class = SalonsSerializer
    permission_classes = [UserPermission]
