from django.urls import path

from . import views


app_name = 'Prestamos'
urlpatterns = [
    path('', views.index, name='index'),
]