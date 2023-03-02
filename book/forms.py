from django import forms
from django.forms import ModelForm
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book
from datetime import date
import datetime



# Create a Booking form
class BookForm(ModelForm):
    """
    This is a custom form class BookForm that is designed to create a form for
    booking a restaurant table.

    The form is created using Django's built-in ModelForm, which is a shortcut
    for creating a form based on an existing model. In this case, the Book
    model is used as the basis for the form.

    The form includes several fields, such as name, phone, email, book_date,
    book_time, people, and message. Each of these fields is defined as a forms
    class with various attributes such as widgets, attrs, and placeholders.

    Number of People input field will now be an integer field with a maximum
    value of 20 and a maximum of 2 digits. The field will also include a
    validator to ensure that the input does not exceed 20.

    The Meta class is used to specify the model used for the form and the
    fields that should be included in the form. The labels and widgets
    dictionaries are used to customize the labels and widgets of the
    form fields, respectively.

    Overall, this BookForm class is used to generate a HTML form that users
    can use to make a booking for a restaurant table, with customized
    validation and visual attributes for each form field.
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

        # Check if a reservation already exists for the given date
        reservations = Book.objects.filter(book_date=book_date)
        if self.instance:
            # Exclude the current reservation if updating an existing reservation
            reservations = reservations.exclude(id=self.instance.id)
        if reservations.exists():
            raise ValidationError('You have already reserved a table for this date.')

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
            open_time = datetime.time(10, 0)  # Replace with actual opening time
            close_time = datetime.time(22, 0)  # Replace with actual closing time
            if book_time < open_time:
                raise ValidationError(f'Booking time must be after {open_time.strftime("%I:%M %p")}')
            elif book_time > close_time:
                raise ValidationError(f'Booking time must be before {close_time.strftime("%I:%M %p")}')
        return book_time

    people = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Number of people',
               'max': 20}),
        validators=[MaxValueValidator(20)],
        max_value=20,
        min_value=1,)
  
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
    This is a custom form class RegisterUserForm inherited from Django's built-
    in UserCreationForm. It is designed to extend the functionality of the
    base class by adding email, first_name, and last_name fields.

    The email, first_name, and last_name fields are declared as forms.
    EmailField and forms.CharField respectively, and each has a widget
    that defines its visual presentation in the HTML form. The widgets
    are set with the attrs dictionary, which contains a CSS class to
    apply to the form input fields.

    The Meta class defines the model that this form is associated with,
    as well as the fields that should be included in the form.
    The password1 and password2 fields are inherited from the base class
    and represent the password and password confirmation fields.

    The clean_email method performs custom validation on the email field.
    It checks if the email already exists in the User model using the User.
    objects.filter() method. If it exists, a ValidationError is raised.

    The __init__ method is used to customize the widget attributes of
    the username, password1, and password2 fields, setting the class attribute
    to 'form-control' for each of them. This adds a CSS class to the input
    fields, making them visually consistent with the other form fields.
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
