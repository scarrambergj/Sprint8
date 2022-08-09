from django.urls import path

from . import views


app_name = 'Tarjetas'
urlpatterns = [
    path('', views.index, name='index'),
]