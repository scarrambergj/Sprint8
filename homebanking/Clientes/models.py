from unicodedata import decimal
from django.db import models

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo = models.ForeignKey('TiposDeCliente', on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return '{} {}'.format(self.customer_name,self.customer_surname)

class TiposDeCliente(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True)
    nombre_tipo = models.TextField()
    tarjetas_de_debito = models.TextField(blank=True, null=True)  # This field type is a guess.
    caja_de_ahorro = models.TextField(blank=True, null=True)  # This field type is a guess.
    caja_de_ahorro_usd = models.TextField()
    descubierto = models.IntegerField()
    tarjetas_de_credito = models.IntegerField()
    retiro_de_efectivo = models.IntegerField()
    chequeras = models.IntegerField()
    comision_por_transferencia = models.DecimalField(max_digits = 5, decimal_places = 2)
    max_transferencias = models.IntegerField(blank=True, null=True)
    max_prestamo = models.IntegerField(null=True, blank = True)

    class Meta:
        db_table = 'tipos_de_cliente'
    
    def __str__(self):
        return self.nombre_tipo
