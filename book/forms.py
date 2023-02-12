from django import forms
from django.forms import ModelForm
from .models import Book


# Create a Booking form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'phone', 'branch', 'book_date', 'people', 'message')

        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'branch': 'Branch',
            'book_date': 'Date',
            'people': 'How many People',
            'message': 'Note',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'branch': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Which branch'}),
            'book_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# of people'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }
