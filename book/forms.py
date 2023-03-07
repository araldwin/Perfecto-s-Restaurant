from django import forms
from django.forms import ModelForm
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book
from datetime import date
import datetime


class BookForm(ModelForm):
    """
    A form used to book a table in a restaurant application.

    Attributes:
    -----------
    book_date : DateField
        A field for selecting the date of the booking.
    book_time : TimeField
        A field for selecting the time of the booking.
    people : IntegerField
        A field for selecting the number of people for the booking.

    Methods:
    --------
    clean_book_date():
        Validates that the selected date is not in the past.
    clean_book_time():
        Validates that the selected time is within the opening
        hours of the restaurant.

    Meta:
    ----
    model : Book
        The model to use for this form.
    fields : tuple
        The fields to include in the form.
    labels : dict
        The labels to use for each field.
    widgets : dict
        The widgets to use for each field.
    """
    book_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control',
                   'placeholder': 'Date'}
        ),
    )

    def clean_book_date(self):
        book_date = self.cleaned_data.get('book_date')
        if book_date and book_date < date.today():
            raise ValidationError('Book date cannot be in the past')
        return book_date

    book_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'type': 'time', 'step': 60, 'class': 'form-control',
                   'placeholder': 'Time'}
        )
    )

    def clean_book_time(self):
        book_time = self.cleaned_data.get('book_time')
        if book_time:
            open_time = datetime.time(10, 0)
            close_time = datetime.time(19, 0)
            if book_time < open_time or book_time > close_time:
                raise ValidationError("You can only reserve a table between "
                                      "10:00 to 19:00.")
        return book_time

    people = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Maximum of 10 per reservation',
                'max': 10
            }
        ),
        validators=[MaxValueValidator(20)],
        max_value=10,
        min_value=1,
    )

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
                                    'placeholder': 'Your Full name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Your Phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Please add your message and request here...'
                }),
        }


class RegisterUserForm(UserCreationForm):
    """
    A Django form used to register new users in an application,
    based on the built-in UserCreationForm.

    Attributes:
    ----------
    email: forms.EmailField
        Field for user email input, with an email
        input widget and CSS class form-control.
    first_name: forms.CharField
        Field for user first name input, with a text
        input widget and CSS class form-control.
    last_name: forms.CharField
        Field for user last name input, with a text
        input widget and CSS class form-control.

    Meta:
    ----
    model: User
        The user model to use for the form.
    fields: tuple
        The fields to include in the form.

    Methods:
    -------
    clean_email()
        Validates the email field and raises a validation
        error if the email is already in use.
    init(self, *args, **kwargs)
        Initializes the form and sets the CSS classes for
        the username, password1, and password2 fields.
    """
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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address already exists.")
        return email

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
