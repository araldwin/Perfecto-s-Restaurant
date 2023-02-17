from django.shortcuts import render, redirect
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
        if form.is_valid():
            form.save()
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


def list_reservation(request):
    # reservation_list = Book.objects.all().order_by('book_date')
    reservation_list = Book.objects.all()

    # Pagination
    # Show 1 reservation per page.
    paginator = Paginator(Book.objects.all(), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'book/reservation_list.html', {'reservation_list': reservation_list, 'page_obj':  page_obj})


