from Cuentas.serializers import CuentaSerializer
from Clientes.serializers import ClienteSerializer, SucursalSerializer, DireccionSerializer
from Prestamos.serializers import PrestamoSerializer
from Tarjetas.serializers import TarjetaPorClienteSerializer, TarjetaSerializer
from rest_framework import viewsets, permissions
from Cuentas.models import Cuenta
from Clientes.models import Cliente, Sucursal, Direcciones
from Prestamos.models import Prestamo
from Tarjetas.models import Tarjetas
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status





class CuentasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            cuentas = Cuenta.objects.all()
            return cuentas
        else:
            id = self.request.user.cliente.customer_id
            cuentas = Cuenta.objects.filter(customer_id=id)
            return cuentas


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            cliente = Cliente.objects.all()
            return cliente
        else:
            id = self.request.user.cliente.customer_id
            cliente = Cliente.objects.filter(customer_id=id)
            return cliente


class PrestamosViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def has_permission(self, request, view):
        if not self.request.user.empleado == '' or  not self.request.user.empleado == None:
            return True

    def get_queryset(self):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            prestamos = Prestamo.objects.all()
            return prestamos
        else:
            id = self.request.user.cliente.customer_id
            prestamos = Prestamo.objects.filter(customer_id=id)
            return prestamos

    def perform_create(self, serializer):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            serializer.save()
            prestamo = Prestamo.objects.filter(loan_id=serializer.data['loan_id'])
            cuenta = Cuenta.objects.filter(customer_id=serializer.data['customer_id']).first()
            total =  prestamo.values('loan_total').get()['loan_total']
            cuenta.balance += int(total)
            cuenta.save()
        else:
            raise Exception('Error, no tiene permisos suficientes')

    def perform_destroy(self, instance):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            prestamo = Prestamo.objects.filter(loan_id=instance.loan_id)
            cuenta = Cuenta.objects.filter(customer_id=instance.customer_id.customer_id).first()
            total =  prestamo.values('loan_total').get()['loan_total']
            cuenta.balance -= int(total)
            cuenta.save()  
            print(prestamo)
            instance.delete()
        else:
            raise Exception('Error, no tiene permisos suficientes')
          


class PrestamosPorSucursal(APIView):
    def get(self, request, pk):
        prestamos = Prestamo.objects.prefetch_related('customer_id').filter(customer_id__branch_id__pk=pk)
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SucursalSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
       if not self.request.user.empleado == None or self.request.user.is_staff:
            sucursales = Sucursal.objects.all()
            return sucursales

class TarjetasPorClienteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TarjetaPorClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            cliente = Cliente.objects.all()
            return cliente

class TarjetasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            tarjetas = Tarjetas.objects.all()
            return tarjetas

class DireccionesViewSet(viewsets.ModelViewSet):
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if not self.request.user.empleado == None or self.request.user.is_staff:
            direcciones = Direcciones.objects.all()
            return direcciones
        else:
            id = self.request.user.cliente.customer_id
            direcciones = Direcciones.objects.filter(cliente=id)
            return direcciones

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        id = instance.cliente.pk
        if  self.request.user.empleado != None or self.request.user.is_staff or self.request.user.cliente.customer_id == id:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        else:
            raise Exception('Error')
        
        

        
    




