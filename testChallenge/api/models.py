from statistics import mode
from tkinter import commondialog
from turtle import circle
from django.db import models
from django.forms import CharField

# Create your models here.
class Client(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()
    ci = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length = 254)
    addres = models.CharField(max_length=255)
    nit = models.IntegerField()
    nationality = models.CharField(max_length=255)

class Room(models.Model):
    codigo = models.CharField(max_length=255)
    nroBeds = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=255)

class Reserve(models.Model):
    class TransactionStatus(models.TextChoices):
        PENDIENTE = "PENDIENTE"
        PAGADO = "PAGADO"
        ELIMINADO = "ELIMINADO"

    status = models.CharField(
        max_length=100,                                                   choices=TransactionStatus.choices,
        default=TransactionStatus.PENDIENTE
    )
    startDate = models.DateField()
    endDate = models.DateField()
    refCliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    refRoom = models.ForeignKey(Room, on_delete=models.CASCADE)

class Factura(models.Model):
    nit = models.CharField(max_length=255)
    razonSocial = models.CharField(max_length=255)
    expedidoDate = models.DateField()

class Payment(models.Model):
    amount = models.FloatField()
    methodPay = models.CharField(max_length=255)
    refReserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    refFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)