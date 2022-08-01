import json
from django.views import View
from django.http import JsonResponse,  HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Client
from .models import Room
from .models import Reserve
from .models import Payment
from .models import Factura
from .serializers import ClientSerializer, ReserveSerializer
from .serializers import RoomSerializer

# Create your views here.

class ClienteViewController(APIView):

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
                refCliente=toJsonData['refCliente'],
                refRoom=toJsonData['refRoom'],
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
        reserves = list(Reserve.objects.filter(id=id).values())
        if len(reserves) > 0:
            Reserve.objects.filter(id=id).delete()
            return Response({"message":"success item was delete"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item was not delete"}, status=status.HTTP_400_BAD_REQUEST)
