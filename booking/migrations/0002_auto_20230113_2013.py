# Generated by Django 3.2.16 on 2023-01-13 20:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gender',
            name='gender',
        ),
        migrations.AddField(
            model_name='gender',
            name='gender_choices',
            field=models.CharField(choices=[('MA', 'Male'), ('FE', 'Female'), ('OT', 'Other')], default='MA', max_length=2),
        ),
        migrations.AlterField(
            model_name='book_appointment',
            name='age',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)]),
        ),
    ]