from django.db import models

# allows you to work with dates and times
from datetime import datetime
# allows you to work with time zones
from django.utils import timezone
# allows you to use Django's built-in user authentication functionality in your application,
from django.contrib.auth.models import User


now = timezone.now()
'''
creates a variable named now that stores the current date and time in the timezone specified 
by the Django project settings (usually the timezone of the server running the Django application).
'''



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
    email = models.EmailField('Email', blank=True, max_length=50)
    book_date = models.DateField(default=datetime.now)
    book_time = models.TimeField(default=datetime.now)
    people = models.CharField('# of Guest', max_length=2)
    message = models.TextField(blank=True)
    

    # allows to pop up on the page and it will list the name
    def __str__(self):
        return self.name
