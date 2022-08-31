from rest_framework import serializers
from Clientes.models import Cliente
from .models import Tarjetas


class TarjetaPorClienteSerializer(serializers.HyperlinkedModelSerializer):
    tarjetas = serializers.HyperlinkedRelatedField(many=True, view_name='tarjetas-detail', read_only=True)

    class Meta:
        model = Cliente
        fields = ['customer_name', 'customer_surname', 'tarjetas']

class TarjetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarjetas
        fields = '__all__'