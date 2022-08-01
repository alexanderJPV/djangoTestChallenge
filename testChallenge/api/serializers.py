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
    # refCliente = serializers.RelatedField(source='Reserve', read_only=True)
    # refRoom = serializers.RelatedField(source='Reserve', read_only=True)
    class Meta:
        model = Reserve
        fields = ["status", "startDate", "endDate"]

class PayementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ["amount", "methodPay", "refReserve", "refFactura"]

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ["nit", "razonSocial", "expedidoDate"]
