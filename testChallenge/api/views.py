import json
from django.views import View
from django.http import JsonResponse,  HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ClientSerializer
from .models import Client

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

            serializer = ClientSerializer(data=client)
            print(serializer)
            print("=================>>>>>>>>>>>")
            print(serializer.is_valid())
            if(serializer.is_valid()):
                client.save()
                return Response({"message":"success item was update"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"error item was not update"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"error item not found!!!"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        clients = list(Client.objects.filter(id=id).values())
        if len(clients) > 0:
            Client.objects.filter(id=id).delete()
            return Response({"message":"success item was delete"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error item was not delete"}, status=status.HTTP_400_BAD_REQUEST)
