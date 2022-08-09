from django.urls import path

from . import views


app_name = 'Cuentas'
urlpatterns = [
    path('', views.index, name='index'),
]