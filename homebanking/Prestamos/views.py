from django.contrib import messages
from django.shortcuts import render
from .forms import CreatePrestamo
from .models import Prestamo
from Cuentas.models import Cuenta
from django.contrib.auth.decorators import login_required

@login_required
def index(request, cuenta_id):
    if request.method == 'POST':
        if int(request.POST['monto']) <= request.user.cliente.tipo.max_prestamo:
            form = Prestamo(
                loan_type = request.POST['tipo'].upper(),
                loan_date = '{}-{}-{}'.format(request.POST['fecha_year'], request.POST['fecha_month'], request.POST['fecha_day']),
                loan_total =  request.POST['monto'],
                customer_id =  request.user.cliente.customer_id)
            form.save()
            cuentas = Cuenta.objects.filter(customer_id = request.user.cliente.customer_id).order_by('account_id')
            for indice, elem in enumerate(cuentas):
                cuenta = cuentas[indice + 1 == cuenta_id]
            cuenta.balance += int(request.POST['monto'])
            cuenta.save()
            messages.error(request, 'Prestamo aceptado')
        else:
            messages.error(request, 'El monto ingresado es mayor al permitido segun su clase')
            form = CreatePrestamo()
            cuentas = Cuenta.objects.filter(customer_id = request.user.cliente.customer_id).order_by('account_id')
            for indice, elem in enumerate(cuentas):
                cuenta = cuentas[indice + 1 == cuenta_id]
            return render(request, 'prestamos/index.html', {'form':form, 'cuenta':cuenta, 'id':cuenta_id})    
    
    form = CreatePrestamo()
    cuentas = Cuenta.objects.filter(customer_id = request.user.cliente.customer_id).order_by('account_id')
    for indice, elem in enumerate(cuentas):
        cuenta = cuentas[indice + 1 == cuenta_id]
    return render(request, 'prestamos/index.html', {'form':form, 'cuenta':cuenta, 'id':cuenta_id})

    
