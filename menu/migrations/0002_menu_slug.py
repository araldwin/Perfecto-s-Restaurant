# Generated by Django 3.2.17 on 2023-02-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]