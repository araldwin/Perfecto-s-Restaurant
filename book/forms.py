from django import forms
from django.forms import ModelForm
from .models import Book


# Create a Booking form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"