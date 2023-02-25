from django.db import models
# allows you to work with dates and times
from datetime import datetime, time
# allows you to work with time zones
from django.utils import timezone
from django.contrib.auth.models import User


def get_current_time():
    """
    "get_current_time()" returns the current time as a time object.
     - It uses the "datetime.now()" function to get the current date and
     time as a datetime object.
     - It then calls the "time()" method on the datetime object to extract
     the time component as a time object.
     - it returns the time object as the result of the function.

     when the function "get_current_time()" is called, it returns the current
     time as a time object. This is useful when setting a default value for a
     TimeField in a Django model, as the TimeField expects a time object as
     its value.

    """
    return datetime.now().time()


class Book(models.Model):
    '''
    This class defines a model for a Book object,
    which represents a reservation made by a guest at a restaurant.
    ---------------------------------------------------------------
    The __str__ method is defined to return the name of the guest,
    which allows Book objects to be represented as
    strings in a human-readable format.
    '''
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField('Guest Name', max_length=50)
    phone = models.CharField('Guest Phone', max_length=50)
    email = models.EmailField('Email', max_length=50)
    book_date = models.DateField(default=datetime.now)
    book_time = models.TimeField(default=get_current_time)
    people = models.CharField('Number of Guest', max_length=2)
    message = models.TextField(blank=True)

    # allows to pop up on the page and it will list the name

    def __str__(self):
        return self.name
