from rest_framework import serializers
from .models import Client
from .models import Room
from .models import Reserve
from .models import Payment
from .models import Factura
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "firstName", "lastName", "age", "ci", "phone", "email", "addres", "nit","nationality"]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "codigo", "nroBeds", "price", "status"]

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ["id", "status", "startDate", "endDate", "refCliente_id", "refRoom_id"]

class PayementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "amount", "methodPay", "refReserve_id", "refFactura_id"]

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ["id", "nit", "razonSocial", "expedidoDate"]
