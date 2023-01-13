from django.contrib import admin
from .models import Book_Appointment
from .models import Gender
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book_Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
