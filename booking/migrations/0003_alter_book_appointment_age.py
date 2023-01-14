# Generated by Django 3.2.16 on 2023-01-14 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230113_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_appointment',
            name='age',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(90)]),
        ),
    ]