from django.shortcuts import render, redirect
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
    return render(request, 'book/add_reservation.html', {'form': form, 'submitted': submitted})


def update_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list-reservation')

    return render(request, 'book/update_reservation.html', {'book': book, 'form':form})


def show_reservation(request, reservation_id):
    book = Book.objects.get(pk=reservation_id)
    return render(request, 'book/show_reservation.html', {'book': book})


def list_reservation(request):
    reservation_list = Book.objects.all()
    return render(request, 'book/reservation_list.html', {'reservation_list':reservation_list})


def home(request):
    return render(request, 'book/home.html', {})
