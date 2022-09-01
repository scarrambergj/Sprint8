from rest_framework import serializers
from .models import Cuenta,TiposDeCuenta

class TipoDeCuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposDeCuenta
        fields = '_all_'

class CuentaSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Cuenta
        fields = ['account_id','balance','iban','tipo']
        
        depth = 1