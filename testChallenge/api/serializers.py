from rest_framework import serializers
from .models import Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["firstName", "lastName", "age", "ci", "phone", "email", "addres", "nit","nationality"]