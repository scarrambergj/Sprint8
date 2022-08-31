from rest_framework import serializers
from .models import Cliente, Direcciones, Sucursal


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

