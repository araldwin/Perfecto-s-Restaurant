from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from book.decorators import unauthenticated_user
from django.contrib.auth.models import Group


@unauthenticated_user
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register_user.html', {'form': form, })


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, ("Invalid login, Please Try Again."))           
    return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been successfully logged out!"))
    return redirect('home')
