from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from food.models import Food
from .forms import RegisterUserForm
from .models import Book
from .forms import BookForm
from django.urls import reverse


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
    return redirect('home')


def home(request):
    food_list = Food.objects.all()
    context = {'food_list': food_list}
    return render(request, 'home.html', context)


def add_reservation(request):
    submitted = False
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            existing_reservations = Book.objects.filter(
                user=request.user,
                book_date=form.cleaned_data['book_date'],
            )
            if existing_reservations.exists():
                form.add_error('book_date',
                               'You have already reserved a table for this '
                               'date.')
            else:
                # If no reservation exists, create a new one for the user
                book = form.save(commit=False)
                book.user = request.user
                book.save()
                return redirect(reverse('add-reservation') + '?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_reservation.html', {'form': form, 'submitted': submitted})


# Reservation_list page


@login_required
def list_reservation(request):
    """
    A view that displays a list of reservations made by the currently logged
    in user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered HTML
        template with the reservation list.

    Raises:
        None.
    """

    reservation_list = (
        Book.objects
        .filter(user=request.user)
        .order_by('book_date')
    )

    # Pagination
    # Show 8 reservation per page.
    paginator = Paginator(reservation_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = "a" * page_obj.paginator.num_pages
    return render(request, 'reservation_list.html',
                  {'page_obj':  page_obj,
                   'nums': nums})


def update_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        existing_reservations = Book.objects.filter(
            user=request.user,
            book_date=form.cleaned_data['book_date'],
        ).exclude(pk=reservation_id)
        if existing_reservations.exists():
            form.add_error('book_date',
                           'You have already reserved a table for '
                           'this date.')
        else:
            form.save()
            messages.success(request, 'Reservation updated successfully. '
                                      'We will call back or send an Email '
                                      'to confirm your reservation. '
                                      'Thank you!')
            return redirect('list-reservation')
    else:
        messages.error(request, 'Failed to update reservation. '
                                'Please check the form for errors.')
    return render(
        request,
        'update_reservation.html',
        {'book': book, 'form': form}
    )


def delete_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    book.delete()
    return redirect('list-reservation')
