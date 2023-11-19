from rest_framework import serializers

from apps.salons.models import Salons


class SalonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salons
        fields = "__all__"


class SalonsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salons
        exclude = ['created_at', 'updated_at']
