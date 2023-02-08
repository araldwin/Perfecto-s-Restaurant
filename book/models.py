from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()


class Branch(models.Model):
    name = models.CharField('Branch Name', max_length=120)
    address = models.CharField(max_length=300)
    web = models.URLField('Website Address')
    branch_email = models.EmailField('Branch Email', max_length=50)
    branch_phone = models.CharField('Branch Phone', max_length=50)

    # allows to pop up on the page and it will list the name
    def __str__(self):
        return self.name


class MyRestaurantUser(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', max_length=50)

    # allows to pop up on the page and it will list the name
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    name = models.CharField('Your Name', max_length=50)
    phone = models.CharField('Your Phone', max_length=50)
    branch = models.ForeignKey(Branch, blank=True, null=True, on_delete=models.CASCADE)
    book_date = models.DateTimeField(default=datetime.now)
    people = models.CharField('# of People', max_length=3)
    message = models.TextField(blank=True)
    guest = models.ManyToManyField(MyRestaurantUser, blank=True)

    # allows to pop up on the page and it will list the name
    def __str__(self):
        return self.name
