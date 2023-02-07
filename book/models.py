from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()


class Book(models.Model):
    name = models.CharField('Your Name', max_length=50)
    email = models.EmailField('Your Email', max_length=50)
    phone = models.CharField('Your Phone', max_length=50)
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
    people = models.CharField('# of People', max_length=3)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name