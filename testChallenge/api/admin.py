from django.contrib import admin
from .models import Client
from .models import Room
from .models import Reserve
from .models import Payment
from .models import Factura
# Register your models here.

admin.site.register(Client)
admin.site.register(Room)
admin.site.register(Reserve)
admin.site.register(Payment)
admin.site.register(Factura)
