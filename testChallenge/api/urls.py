from django.urls import path
from .views import ClienteViewController
from .views import RoomViewController
from .views import ReserveViewController
urlpatterns = [
    # Clients end-points
    path('clients/',ClienteViewController.as_view(), name="clients"),
    path('clients/<int:id>',ClienteViewController.as_view(), name="clients_id_params"),
    # Rooms end-points
    path('rooms/',RoomViewController.as_view(), name="rooms"),
    path('rooms/<int:id>',RoomViewController.as_view(), name="rooms_id_params"),
    # Reserve end-points
    path('reserves/',ReserveViewController.as_view(), name="reserves"),
    path('reserves/<int:id>',ReserveViewController.as_view(), name="reserves_id_params"),
]