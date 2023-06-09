from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerField
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class BookAppointment(models.Model):
    """
    Model to store appointment details
    """

    class GenderChoices(models.TextChoices):
        MALE = 'MA', _('Male')
        FEMALE = 'FE', _('Female')
        OTHER = 'OT', _('Other')

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='appointment'
    )
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    age = models.IntegerField(
        null=False,
        blank=False,
        default=18,
        validators=[
            MinValueValidator(18),
            MaxValueValidator(90)
        ]
    )
    gender = models.CharField(
        max_length=2,
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
    )
    date = models.DateField(null=True, blank=False)
    time = models.TimeField(default=datetime.time(12, 00), blank=False)
    goals = models.TextField(max_length=200, null=True, blank=False)
    health_info = models.TextField(max_length=2000, null=True, blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return str(self.id)

    def gender_choices(self):
        return self.gender in {
            GenderChoices.MALE,
            GenderChoices.FEMALE,
            GenderChoices.OTHER
        }
