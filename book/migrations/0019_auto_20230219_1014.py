# Generated by Django 3.2.17 on 2023-02-19 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_rename_guest_book_myrestaurantuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]