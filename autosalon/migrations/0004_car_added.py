# Generated by Django 5.1.3 on 2024-12-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autosalon', '0003_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='added',
            field=models.DateField(default='2024-12-11'),
        ),
    ]
