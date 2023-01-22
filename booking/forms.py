from .models import BookAppointment
from django import forms


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


class UpdateBooking(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = ('date',
                  'time',
                  'goals',
                  'health_info',)
