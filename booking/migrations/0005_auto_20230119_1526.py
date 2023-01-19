# Generated by Django 3.2.16 on 2023-01-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20230119_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='gender',
            field=models.CharField(choices=[('MA', 'Male'), ('FE', 'Female'), ('OT', 'Other')], default='MA', max_length=2),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]