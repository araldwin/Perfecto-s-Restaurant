from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.models import Group
from book.models import MyRestaurantUser


def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))
			return redirect('login')

	else:
		return render(request, 'registration/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('home')


def register_user(request):
	form = RegisterUserForm(request.POST)
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='myrestaurantuser')
			user.groups.add(group)
			MyRestaurantUser.objects.create(user=user, first_name=user.first_name, last_name=user.last_name)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')

	return render(request, 'registration/register_user.html', {
            'form': form,
        })
