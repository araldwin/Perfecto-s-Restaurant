from django import forms
from django.forms import ModelForm
from .models import Book
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

    The clean_people method is used to perform custom validation on the
    people field, which is intended to capture the number of people for
    the reservation. The method checks whether the value entered is an
    integer greater than zero, raising a ValidationError if not.

    The Meta class is used to specify the model used for the form and the
    fields that should be included in the form. The labels and widgets
    dictionaries are used to customize the labels and widgets of the
    form fields, respectively.

    Overall, this BookForm class is used to generate a HTML form that users
    can use to make a booking for a restaurant table, with customized
    validation and visual attributes for each form field.
    """

    def clean_people(self):

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
                                      'placeholder': 'Number of people'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                      'placeholder': 'Your Message'}),
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