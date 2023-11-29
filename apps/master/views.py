from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from apps.master.models import Master
from apps.master.serializers import MasterRegisterSerializer, MasterRetriveSerializer


class MasterRegisterCreateAPIView(CreateAPIView):
    serializer_class = MasterRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MasterInfoView(ListAPIView):
    # permission_classes = [MasterPermission]
    serializer_class = MasterRetriveSerializer

    def get_queryset(self):
        master = self.request.user
        print(master)
        if master.is_authenticated:
            if master.is_superuser:
                return Master.objects.all()
            elif hasattr(master, 'master'):
                return Master.objects.filter(id=master.id)
            else:
                return Master.objects.filter(id=master.id)
        else:
            return Master.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
