from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm


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
    return render(request, 'book/add_reservation.html', {'form': form, 'submitted':submitted})


def all_reservations(request):
    reservation_list = Book.objects.all()
    return render(request, 'book/reservation_list.html', {'reservation_list': reservation_list})


def home(request):
    return render(request, 'book/home.html', {})
