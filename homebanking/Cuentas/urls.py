from django.urls import path, include

from . import views


app_name = 'Cuentas'
urlpatterns = [
    path('<int:cuenta_id>/', views.index, name='index'),
    path('<int:cuenta_id>/cambiar-cuenta', views.cuentas, name = 'cuentas'),
    path('<int:cuenta_id>/ayuda', views.ayuda, name='ayuda'),
]