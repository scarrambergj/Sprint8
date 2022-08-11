from django.urls import path, include

from . import views


app_name = 'Cuentas'
urlpatterns = [
    path('', views.index, name='index'),
]