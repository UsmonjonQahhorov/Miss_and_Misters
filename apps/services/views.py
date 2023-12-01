from rest_framework.generics import CreateAPIView, DestroyAPIView,RetrieveAPIView,UpdateAPIView
from apps.services.models import Services
from apps.services.permissions import ServicePermision
from apps.services.serializers import ServiceCreateSerializer


class ServiceCreateAPIView(CreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermision]


class ServiceGetAPIView(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermision]


class ServiceDeleteAPIView(DestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermision]


class ServiceUpdateAPIView(UpdateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [ServicePermision]

