from django.urls import path

from . import views


app_name = 'Home'
urlpatterns = [
    path('', views.home, name='home'),
    path('ayuda', views.ayuda, name='ayuda'),
]