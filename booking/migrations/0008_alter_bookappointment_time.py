# Generated by Django 3.2.16 on 2023-01-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20230121_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
