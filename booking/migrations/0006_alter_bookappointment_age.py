# Generated by Django 3.2.16 on 2023-01-20 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20230119_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='age',
            field=models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(90)]),
        ),
    ]
