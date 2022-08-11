from django.shortcuts import render
from .forms import CreatePrestamo
from .models import Prestamo
from Cuentas.models import Cuenta

def index(request, cuenta_id):
    if request.method == 'POST':
        form = Prestamo(
            loan_type = request.POST['tipo'].upper(),
            loan_date = '{}-{}-{}'.format(request.POST['fecha_year'], request.POST['fecha_month'], request.POST['fecha_day']),
            loan_total =  request.POST['monto'],
            customer_id =  request.user.cliente.customer_id)
        form.save()
    form = CreatePrestamo()
    cuentas = Cuenta.objects.filter(customer_id = request.user.cliente.customer_id).order_by('account_id')
    for indice, elem in enumerate(cuentas):
        cuenta = cuentas[indice + 1 == cuenta_id]
    return render(request, 'prestamos/index.html', {'form':form, 'cuenta':cuenta, 'id':cuenta_id})


