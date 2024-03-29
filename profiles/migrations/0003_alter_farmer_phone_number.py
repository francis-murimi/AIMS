# Generated by Django 4.2.10 on 2024-02-12 17:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_farmer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must start with '254' and contain 12 digits (including country code).", regex='^\\254\\d{9}$')]),
        ),
    ]
