from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
import datetime


# Create your models here.

GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER'),
)


class Gender(models.Model):
    """
    Model for creating the gender dropdown list
    Source: https://stackoverflow.com/questions/31130706/dropdown-in-django-model
    """
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='')


class Book_Appointment(models.Model):
    """
    Model to store appointment details
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        validators=[
            MinValueValidator(18),
            MaxValueValidator(90)
            ]
        )
    gender = models.ForeignKey(
        Gender, on_delete=models.CASCADE, related_name='appointment'
        )
    date_time = models.DateTimeField()
    goals = models.TextField(max_length=200, null=True)
    health_info = models.TextField(max_length=2000, null=True)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField()

    def __str__(self):
        return str(self.id)
