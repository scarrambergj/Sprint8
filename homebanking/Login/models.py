from django.db import models
from django.contrib.auth.models import AbstractUser
from Clientes.models import Cliente

class User(AbstractUser):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
