from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Book, MyRestaurantUser
from .forms import BookForm
from django.contrib.auth.decorators import login_required

# Import Pagination
from django.core.paginator import Paginator


def home(request):
    return render(request, 'book/home.html', {})


def delete_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    book.delete()
    return redirect('list-reservation')



def add_reservation(request):
    submitted = False
    if request.method == "POST":
        form = BookForm(request.POST)
        # when user add_reservatation it will be automatic myrestaurant user
        if form.is_valid():
            book = form.save(commit=False)
            book.myrestaurantuser = request.user.myrestaurantuser
            book.save()
            return HttpResponseRedirect('/add_reservation?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'book/add_reservation.html', {'form': form, 'submitted': submitted})


def update_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list-reservation')

    return render(request, 'book/update_reservation.html', {'book': book, 'form': form})


def show_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    return render(request, 'book/show_reservation.html', {'book': book})


# Reservation_list page

@login_required
def list_reservation(request):
    reservation_list = Book.objects.filter(myrestaurantuser__user=request.user)

    # Pagination
    # Show 5 reservation per page.
    paginator = Paginator(reservation_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/reservation_list.html', {'reservation_list': reservation_list, 'page_obj':  page_obj})


