from django import forms
from django.forms import ModelForm
from .models import Book


# Create a Booking form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'phone', 'branch', 'book_date', 'people', 'message')

        labels = {
            'name': '',
            'phone': '',
            'branch': '',
            'book_date': '',
            'people': '',
            'message': '',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch'}),
            'book_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# of people'}),
            'message': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }
