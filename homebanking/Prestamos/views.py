from django.shortcuts import render
from .forms import CreatePrestamo
from .models import Prestamo
from Clientes.models import Cliente

def index(request):
    if request.method == 'POST':
        form = Prestamo(
            loan_type = request.POST['tipo'].upper(),
            loan_date = '{}-{}-{}'.format(request.POST['fecha_year'], request.POST['fecha_month'], request.POST['fecha_day']),
            loan_total =  request.POST['monto'],
            customer_id =  request.user.cliente.customer_id)
        form.save()
    form = CreatePrestamo()
    return render(request, 'prestamos/index.html', {'form':form})
