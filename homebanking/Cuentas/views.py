from django.shortcuts import render,  get_object_or_404
from .models import Cuenta


def index(request, cuenta_id):
    cuentas = Cuenta.objects.filter(customer_id = request.user.cliente.customer_id).order_by('account_id')
    for indice, elem in enumerate(cuentas):
        cuenta = cuentas[indice == cuenta_id]
    return render(request, 'cuentas/index.html', {'cuenta':cuenta, 'id':cuenta_id + 1})
