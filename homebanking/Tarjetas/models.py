from django.db import models

class Tarjetas(models.Model):
    tarjeta_id = models.AutoField(primary_key=True, blank=True)
    numero = models.IntegerField(unique=True)
    cvv = models.IntegerField()
    fecha_otorgamiento = models.TextField()
    fecha_expiracion = models.TextField()
    tipo = models.TextField()
    marca = models.ForeignKey('MarcasDeTarjeta', on_delete=models.CASCADE, blank=True, null=True)
    cliente = models.ForeignKey('Clientes.Cliente',  related_name='tarjetas', on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = 'tarjetas'
        verbose_name_plural = "Tarjetas"

class MarcasDeTarjeta(models.Model):
    marca_id = models.AutoField(primary_key=True, blank=True)
    nombre_marca = models.TextField()

    class Meta:
        db_table = 'marcas_de_tarjeta'