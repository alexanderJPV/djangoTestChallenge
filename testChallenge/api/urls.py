from django.urls import path
from .views import ClienteViewController

urlpatterns = [
    path('clients/',ClienteViewController.as_view(), name="clients"),
    path('clients/<int:id>',ClienteViewController.as_view(), name="clients_with_params")
]