from django.db import models

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo = models.ForeignKey('TiposDeCuenta', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'cuenta'

    def __str__(self):
        return self.account_id

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI') 
    branch_id = models.IntegerField()

    class Meta:
        db_table = 'empleado'
    
    def __str__(self):
        return '{} {}'.format(self.employee_name,self.employee_surname)

class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True)
    numero_de_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.TextField(blank=True, null=True)
    tipo_de_operacion = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'movimientos'
        verbose_name_plural = "Movimientos"

class TiposDeCuenta(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True)
    nombre_cuenta = models.TextField()

    class Meta:
        db_table = 'tipos_de_cuenta'

