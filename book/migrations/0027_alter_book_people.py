# Generated by Django 3.2.18 on 2023-02-25 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0026_alter_book_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='people',
            field=models.IntegerField(max_length=2, verbose_name='# of Guest'),
        ),
    ]
