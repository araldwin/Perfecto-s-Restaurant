from django import forms
from django.forms import ModelForm
from .models import Book
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create a Booking form
class BookForm(ModelForm):

    def clean_people(self):
        '''
        a custom validation to to ensure that 
        the people field is a positive integer.
        '''

        data = self.cleaned_data['people']
        try:
            value = int(data)
            if value <= 0:
                raise ValidationError("Please enter the number of guests.")
        except ValueError:
            raise ValidationError("Invalid value for number of people.")
        return value

    book_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date'})
    )
    book_time = forms.TimeField(widget=forms.TimeInput(
        attrs={'type': 'time', 'step': 60, 'class': 'form-control',
                                                    'placeholder': 'Time'}))

    class Meta:
        model = Book
        fields = ('name', 'phone', 'book_date', 'email',
                  'book_time', 'people', 'message')

        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'email': 'Email',
            'book_date': 'Date',
            'book_time': 'Time',
            'people': 'How many People',
            'message': 'Note',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Your Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Your Email'}),
            'people': forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': '# of people'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                      'placeholder': 'Your Message'}),
        }


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
