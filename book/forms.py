from django import forms
from django.forms import ModelForm
from .models import Book


# Create a Booking form
class BookForm(ModelForm):
    book_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date'}))
    book_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'step': 60, 'class': 'form-control', 'placeholder': 'Time'}))

    class Meta:
        model = Book
        fields = ('name', 'phone', 'branch', 'book_date', 'book_time', 'people', 'message')

        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'branch': 'Branch',
            'book_date': 'Date',
            'book_time': 'Time',
            'people': 'How many People',
            'message': 'Note',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
            'branch': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Which branch'}),
            'people': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# of people'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }