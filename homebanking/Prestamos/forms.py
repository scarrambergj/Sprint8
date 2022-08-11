from dataclasses import field
from django import forms
from .models import Prestamo

class CreatePrestamo(forms.Form):
    tipo = forms.ChoiceField(label='Tipo de prestamo', choices = (('Hipotecario', 'Hipotecario'),('Personal', 'Personal'),('Prendario', 'Prendario')), required=True)
    fecha= forms.DateField(label='Fecha de inicio', widget=forms.SelectDateWidget, input_formats=["%YY-%MM-%DD"], required=True)
    monto = forms.IntegerField(label = "Monto", required=True)

    class Meta:
        model: Prestamo
        fields = '__all__'
