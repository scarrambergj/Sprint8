from dataclasses import fields
from rest_framework import serializers

from Clientes.models import Sucursal
from .models import Prestamo
from Clientes.models import Sucursal, Cliente
from Cuentas.models import Cuenta


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'


class PrestamosPorSucursal(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sucursal
        fields = '__all__'