from tkinter import CASCADE
from django.db import models

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True, blank=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey('Clientes.Cliente', related_name='cliente', on_delete=models.CASCADE)

    class Meta:
        db_table = 'prestamo'
