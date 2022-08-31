from django.db import models
from django.contrib.auth.models import AbstractUser
from Clientes.models import Cliente
from Cuentas.models import Empleado

class User(AbstractUser):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, blank=True, null=True)
