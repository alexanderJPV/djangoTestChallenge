from rest_framework import serializers
from .models import Client
from .models import Room
from .models import Reserve
from .models import Payment
from .models import Factura
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["firstName", "lastName", "age", "ci", "phone", "email", "addres", "nit","nationality"]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["codigo", "nroBeds", "price", "status"]

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ["status", "startDate", "endDate", "refCliente_id", "refRoom_id"]

class PayementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["amount", "methodPay", "refReserve_id", "refFactura_id"]

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ["nit", "razonSocial", "expedidoDate"]
