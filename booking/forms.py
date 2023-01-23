from django import forms
from django.forms import ModelForm
from .models import BookAppointment


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'text'


class AddBooking(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = ('first_name',
                  'last_name',
                  'age',
                  'gender',
                  'date',
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


class UpdateBooking(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = ('date',
                  'time',
                  'goals',
                  'health_info',)
