from django.contrib import admin
from .models import Book_Appointment, Gender
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['gender_choices']


@admin.register(Book_Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'date_time')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ('first_name', 'last_name', 'email', 'date_time', 'created_on', 'updated_on')
    summernote_fields = ('goals', 'health_info')
    actions = ['approve_bookings']

    def approve_comments(self, request, queryset):
        queryset.update(apporved=True)
