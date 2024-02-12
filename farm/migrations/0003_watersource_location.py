# Generated by Django 5.0.1 on 2024-02-12 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0002_soil_watersource_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='watersource',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sources', to='farm.village'),
        ),
    ]