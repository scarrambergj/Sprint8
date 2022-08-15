from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
import random
from Clientes.models import Cliente

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	cliente = random.randrange(0, Cliente.objects.values_list('customer_id').count())

	

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		help_texts = {
            'username': None,
		}
	def __init__(self, *args, **kwargs): 
		super(NewUserForm, self).__init__(*args, **kwargs) 
		 
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None
		self.fields['password1'].label = ('Contraseña')
		self.fields['password2'].label = ('Confirmación de contraseña')
		self.fields['username'].label = ('Nombre de usuario')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.cliente = Cliente.objects.get(pk = self.cliente)

		if commit:
			user.save()
		return user