from django.shortcuts import  render
from .forms import NewUserForm, NewEmpleadoForm
from Cuentas.models import Cuenta
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			cliente_id = user.cliente.customer_id
			if Cuenta.objects.filter(customer_id=cliente_id):
				messages.success(request, 'Successful registration.')
				return HttpResponseRedirect(reverse('login:login'))
			else:
				user.delete()
				messages.error(request, "Unsuccessful registration. You need to open an account to access homebanking.")
				return HttpResponseRedirect(reverse('login:register'))
				
		else:		
			messages.error(request, "Unsuccessful registration. Invalid information.")
			return HttpResponseRedirect(reverse('login:register'))
	else:
		
		form = NewUserForm()
		return render (request,"login/register.html",{"form":form})


def registerEmpleado(request):
	if request.method == "POST":
		form = NewEmpleadoForm(request.POST)
		if form.is_valid():
			user = form.save()
			
			messages.success(request, 'Successful registration.')
			return HttpResponseRedirect(reverse('login:login'))
			
				
		else:		
			messages.error(request, "Unsuccessful registration. Invalid information.")
			return HttpResponseRedirect(reverse('login:registerEmpleado'))
	else:
		
		form = NewEmpleadoForm()
		return render (request,"login/registerEmpleado.html",{"form":form})

