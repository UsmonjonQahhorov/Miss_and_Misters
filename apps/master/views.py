from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.response import Response

from apps.master.models import Master
from apps.master.serializers import MasterRegisterSerializer, CheckMActivationCodeSerializer, MasterRetriveSerializer
from apps.users.models import getKey


class MasterRegisterCreateAPIView(CreateAPIView):
    serializer_class = MasterRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CheckActivationCodeAPIView(GenericAPIView):
    serializer_class = CheckMActivationCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user_data = getKey(key=data['email'])
        print(f"View: {user_data}")
        if not user_data or user_data['activate_code'] != data['activation_code']:
            return Response({"error": "Error activating user. Invalid activation code or email."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = user_data['master']
        user.is_verified = True
        user.is_active = True
        user.save()

        return Response({"message": "Your email has been confirmed"}, status=status.HTTP_200_OK)


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
