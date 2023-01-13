from django.contrib import admin
from .models import Book_Appointment
from .models import Gender

admin.site.register(Gender)
admin.site.register(Book_Appointment)