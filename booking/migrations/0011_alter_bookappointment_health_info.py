# Generated by Django 3.2.19 on 2023-06-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_bookappointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='health_info',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
