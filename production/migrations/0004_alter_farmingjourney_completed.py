# Generated by Django 4.2.10 on 2024-02-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_farmingjourney'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmingjourney',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
