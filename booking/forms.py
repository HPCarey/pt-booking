from django import forms
from django.forms import ModelForm
from .models import BookAppointment
from django.utils import timezone
import datetime


class DateInput(forms.DateInput):
    """
    Class to make a calender show when choosing the date.
    See sources in README
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'text'


class AddBooking(forms.ModelForm):
    """
    Creates the form to be rendered for add_booking view
    """
    class Meta:
        model = BookAppointment
        fields = (
            'first_name',
            'last_name',
            'age',
            'gender',
            'date',
            'time',
            'goals',
            'health_info',
        )

        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_age(self):
        """
        Check if age is less 18 or more than 90
        Raise a custom error message if so
        """
        age = self.cleaned_data.get('age')

        if age < 18:
            raise forms.ValidationError("You must be at least 18 years old.")

        if age > 90:
            raise forms.ValidationError(
                "You cannot be more than 90 years old."
            )

        return age

    def clean_date(self):
        """
        Check if date user inputs is in the past
        Raise an error if date is in the past
        Otherwise, return the chosen date
        """
        date = self.cleaned_data.get('date')

        if date:
            current_date = timezone.now().date()
            if date < current_date:
                raise forms.ValidationError("Cannot book a date in the past.")

        return date


class UpdateBooking(forms.ModelForm):
    """
    Creates the form to be rendered for update_booking view
    """
    class Meta:
        model = BookAppointment
        fields = ('date',
                  'time',
                  'goals',
                  'health_info',)
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_date(self):
        """
        Check if date user inputs is in the past
        Raise an error if date is in the past
        Otherwise, return the chosen date
        """
        date = self.cleaned_data.get('date')

        if date:
            current_date = timezone.now().date()
            if date < current_date:
                raise forms.ValidationError("Cannot book a date in the past.")

        return date
