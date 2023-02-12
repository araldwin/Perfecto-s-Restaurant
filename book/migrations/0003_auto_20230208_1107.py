# Generated by Django 3.2.17 on 2023-02-08 11:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20230207_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Branch Name')),
                ('address', models.CharField(max_length=300)),
                ('web', models.URLField(verbose_name='Website Address')),
                ('branch_email', models.EmailField(max_length=50, verbose_name='Branch Email')),
                ('branch_phone', models.CharField(max_length=50, verbose_name='Branch Phone')),
            ],
        ),
        migrations.CreateModel(
            name='MyRestaurantUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Your Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Your Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Your Email')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='email',
        ),
        migrations.RemoveField(
            model_name='book',
            name='time',
        ),
        migrations.AddField(
            model_name='book',
            name='book_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='book',
            name='bookings',
            field=models.ManyToManyField(blank=True, to='book.MyRestaurantUser'),
        ),
        migrations.AddField(
            model_name='book',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.branch'),
        ),
    ]