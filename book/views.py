from django.shortcuts import render
from .models import Book


def all_reservations(request):
    reservation_list = Book.objects.all()
    return render(request, 'book/reservation_list.html', {'reservation_list': reservation_list})


def home(request):
    return render(request, 'book/home.html', {})
