from email.mime import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'cliente', views.ClienteViewSet, basename='cliente')
router.register(r'cuentas', views.CuentasViewSet, basename='cuentas')
router.register(r'prestamos', views.PrestamosViewSet, basename='prestamos')
router.register(r'sucursales', views.SucursalViewSet, basename='sucursales')
router.register(r'tarjetasPorCliente', views.TarjetasPorClienteViewSet, basename='tarjetasPorCliente')
router.register(r'tarjetas', views.TarjetasViewSet, basename='tarjetas')
router.register(r'direcciones', views.DireccionesViewSet, basename='direcciones')



urlpatterns = [
    path('', include(router.urls)),
    path('prestamosPorSucursal/<int:pk>', views.PrestamosPorSucursal.as_view(),  name = 'prestamosPorSucursal'),
]