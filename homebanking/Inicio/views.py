from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Se cerró tu sesión")
        return redirect('home:home')
    return render(request, 'inicio/home.html')


