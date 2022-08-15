from django.shortcuts import render
from django.urls import reverse
from .models import Cuenta
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request, cuenta_id):
    cuentas = Cuenta.objects.filter(customer_id = request.user.cliente.customer_id).order_by('account_id')
    for indice, elem in enumerate(cuentas):
        cuenta = cuentas[indice == cuenta_id + 1]
    if cuenta_id > len(cuentas):
        messages.error(request, 'Cuenta no existente')
        return HttpResponseRedirect(reverse('Cuentas:index', args=(1,)))
    else:
        return render(request, 'cuentas/index.html', {'cuenta':cuenta, 'id':cuenta_id})

def cuentas(request, cuenta_id):
    cuentas = Cuenta.objects.filter(customer_id = request.user.cliente.customer_id).order_by('account_id')
    return render(request, 'cuentas/cuentas.html', {'cuentas':cuentas, 'id':cuenta_id})

def ayuda(request, cuenta_id):
    return render(request, 'cuentas/ayuda.html', {'id':cuenta_id})

