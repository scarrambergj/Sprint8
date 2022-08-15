from django.shortcuts import render
from Login.models import User

def home(request):
    return render(request, 'inicio/home.html')


