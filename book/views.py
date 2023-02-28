from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.models import Group
from food.models import Food


# Import Pagination
from django.core.paginator import Paginator


def home(request):
    food_list = Food.objects.all()
    context = {'food_list': food_list}
    return render(request, 'home.html', context)


def delete_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    book.delete()
    return redirect('list-reservation')


def add_reservation(request):
    submitted = False
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # Check if the user has already made a reservation for the given date slot
            existing_reservations = Book.objects.filter(
                user=request.user,
                book_date=form.cleaned_data['book_date'],
            )
            if existing_reservations.exists():
                # If a reservation already exists for the user and time slot, display an error message
                form.add_error(None, 'This time slot is already reserved..')
            else:
                # If no reservation exists, create a new one for the user
                book = form.save(commit=False)
                book.user = request.user
                book.save()
                return HttpResponseRedirect('/add_reservation?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_reservation.html', {'form': form, 'submitted': submitted})


def update_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list-reservation')

    return render(request, 'update_reservation.html',
                  {'book': book, 'form': form})


def show_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    return render(request, 'show_reservation.html', {'book': book})


# Reservation_list page

@login_required
def list_reservation(request):
    '''
     The reservation_list will be filtered by the User corresponding to the currently logged-in user, as specified by request.user.
     The filter expression uses the __ syntax to follow the foreign key relationship to the MyRestaurantUser model, and then to its user field.
    '''
    reservation_list = Book.objects.filter(user=request.user)

    # Pagination
    # Show 5 reservation per page.
    paginator = Paginator(reservation_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reservation_list.html', {'reservation_list': reservation_list, 'page_obj':  page_obj})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Success")
        else:
            return HttpResponse("There Was An Error Logging In, Try Again...")
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
            login(request, user)
            message = 'Registration Successful!'
            return HttpResponse(message, status=200)
        else:
            return HttpResponse(form.as_p(), status=400)

    return render(request, 'registration/register_modal.html', {'form':  form})
