import json
from django.views import View
from django.http import JsonResponse,  HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Client, Room, Reserve, Payment, Factura
from .serializers import ClientSerializer, ReserveSerializer, RoomSerializer, PayementSerializer, FacturaSerializer

# Create your controllers endpoints here.

class ClienteViewController(APIView):

    def greeting(request):
        return HttpResponse("Hello from two path again...........")
    def get(self, request, id=0):
        if(id > 0):
            clients =  list(Client.objects.filter(id=id).values())
            if(len(clients) > 0):
                serializer = ClientSerializer(clients, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            clients =  Client.objects.all().values()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        toJsonData = json.loads(request.body)
        serializer = ClientSerializer(data=toJsonData)
        if serializer.is_valid():
            client = Client.objects.create(
                firstName=toJsonData['firstName'],
                lastName=toJsonData['lastName'],
                age=toJsonData['age'],
                ci=toJsonData['ci'],
                phone=toJsonData['phone'],
                email=toJsonData['email'],
                addres=toJsonData['addres'],
                nit=toJsonData['nit'],
                nationality=toJsonData['nationality'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"error item was not create"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        toJsonData = json.loads(request.body)
        clients = list(Client.objects.filter(id=id).values())
        if len(clients) > 0:
            client = Client.objects.get(id=id)
            client.firstName = toJsonData['firstName']
            client.lastName = toJsonData['lastName']
            client.age = toJsonData['age']
            client.ci = toJsonData['ci']
            client.phone = toJsonData['phone']
            client.email = toJsonData['email']
            client.addres = toJsonData['addres']
            client.nit = toJsonData['nit']
            client.nationality = toJsonData['nationality']
            # serializer = ClientSerializer(data=client)
            # print("======================>>>>>>>>>>>>")
            # print(serializer.is_valid())
            client.save()
            return Response({"message":"success item was update"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        clients = list(Client.objects.filter(id=id).values())
        if len(clients) > 0:
            Client.objects.filter(id=id).delete()
            return Response({"message":"success item was delete"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item was not delete"}, status=status.HTTP_400_BAD_REQUEST)

class RoomViewController(APIView):

    def get(self, request, id=0):
        if(id > 0):
            rooms =  list(Room.objects.filter(id=id).values())
            if(len(rooms) > 0):
                serializer = RoomSerializer(rooms, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            rooms =  Room.objects.all().values()
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        toJsonData = json.loads(request.body)
        serializer = RoomSerializer(data=toJsonData)
        if serializer.is_valid():
            room = Room.objects.create(
                codigo=toJsonData['codigo'],
                nroBeds=toJsonData['nroBeds'],
                price=toJsonData['price'],
                status=toJsonData['status'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"error item was not create"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        toJsonData = json.loads(request.body)
        rooms = list(Room.objects.filter(id=id).values())
        if len(rooms) > 0:
            room = Room.objects.get(id=id)
            room.codigo = toJsonData['codigo']
            room.nroBeds = toJsonData['nroBeds']
            room.price = toJsonData['price']
            room.status = toJsonData['status']
            room.save()
            return Response({"message":"success item was update"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        rooms = list(Room.objects.filter(id=id).values())
        if len(rooms) > 0:
            Room.objects.filter(id=id).delete()
            return Response({"message":"success item was delete"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item was not delete"}, status=status.HTTP_400_BAD_REQUEST)


class ReserveViewController(APIView):

    def get(self, request, id=0):
        if(id > 0):
            reserves =  list(Reserve.objects.filter(id=id).values())
            if(len(reserves) > 0):
                serializer = ReserveSerializer(reserves, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            reserves =  Reserve.objects.all().values()
            serializer = ReserveSerializer(reserves, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        toJsonData = json.loads(request.body)
        serializer = ReserveSerializer(data=toJsonData)
        if serializer.is_valid():
            reserve = Reserve.objects.create(
                status=toJsonData['status'],
                startDate=toJsonData['startDate'],
                endDate=toJsonData['endDate'],
                refCliente_id=toJsonData['refCliente_id'],
                refRoom_id=toJsonData['refRoom_id'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"error item was not create"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        toJsonData = json.loads(request.body)
        reserves = list(Reserve.objects.filter(id=id).values())
        if len(reserves) > 0:
            reserve = Reserve.objects.get(id=id)
            reserve.status = toJsonData['status']
            reserve.startDate = toJsonData['startDate']
            reserve.endDate = toJsonData['endDate']
            reserve.refCliente_id = toJsonData['refCliente_id']
            reserve.refRoom_id = toJsonData['refRoom_id']
            reserve.save()
            return Response({"message":"success item was update"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        reserves = list(Reserve.objects.filter(id=id).values())
        if len(reserves) > 0:
            Reserve.objects.filter(id=id).delete()
            return Response({"message":"success item was delete"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item was not delete"}, status=status.HTTP_400_BAD_REQUEST)

class FacturaViewController(APIView):

    def get(self, request, id=0):
        if(id > 0):
            facturas =  list(Factura.objects.filter(id=id).values())
            if(len(facturas) > 0):
                serializer = FacturaSerializer(facturas, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            facturas =  Factura.objects.all().values()
            serializer = FacturaSerializer(facturas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        toJsonData = json.loads(request.body)
        serializer = FacturaSerializer(data=toJsonData)
        if serializer.is_valid():
            factura = Factura.objects.create(
                nit=toJsonData['nit'],
                razonSocial=toJsonData['razonSocial'],
                expedidoDate=toJsonData['expedidoDate'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"error item was not create"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        toJsonData = json.loads(request.body)
        facturas = list(Factura.objects.filter(id=id).values())
        if len(facturas) > 0:
            factura = Factura.objects.get(id=id)
            factura.nit = toJsonData['nit']
            factura.razonSocial = toJsonData['razonSocial']
            factura.expedidoDate = toJsonData['expedidoDate']
            factura.save()
            return Response({"message":"success item was update"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        facturas = list(Factura.objects.filter(id=id).values())
        if len(facturas) > 0:
            Factura.objects.filter(id=id).delete()
            return Response({"message":"success item was delete"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item was not delete"}, status=status.HTTP_400_BAD_REQUEST)

class PaymentViewController(APIView):

    def get(self, request, id=0):
        if(id > 0):
            payments =  list(Payment.objects.filter(id=id).values())
            if(len(payments) > 0):
                serializer = PayementSerializer(payments, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            payments =  Payment.objects.all().values()
            serializer = PayementSerializer(payments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        toJsonData = json.loads(request.body)
        serializer = PayementSerializer(data=toJsonData)
        if serializer.is_valid():
            payment = Payment.objects.create(
                amount=toJsonData['amount'],
                methodPay=toJsonData['methodPay'],
                refFactura_id=toJsonData['refFactura_id'],
                refReserve_id=toJsonData['refReserve_id'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"error item was not create"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        toJsonData = json.loads(request.body)
        payments = list(Payment.objects.filter(id=id).values())
        if len(payments) > 0:
            payment = Payment.objects.get(id=id)
            payment.amount = toJsonData['amount']
            payment.methodPay = toJsonData['methodPay']
            payment.refFactura_id = toJsonData['refFactura_id']
            payment.refReserve_id = toJsonData['refReserve_id']
            payment.save()
            return Response({"message":"success item was update"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        payments = list(Payment.objects.filter(id=id).values())
        if len(payments) > 0:
            Payment.objects.filter(id=id).delete()
            return Response({"message":"success item was delete"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item was not delete"}, status=status.HTTP_400_BAD_REQUEST)
