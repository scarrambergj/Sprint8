from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout
from django.contrib import messages


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("Home:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="Login/register.html", context={"register_form":form})


