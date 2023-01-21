from django.contrib import admin
from .models import BookAppointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BookAppointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'date', 'time', 'created_on', 'updated_on')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ('first_name', 'last_name', 'email', 'date')
    summernote_fields = ('goals', 'health_info')
    actions = ['approve_bookings']

    def approve_comments(self, request, queryset):
        queryset.update(apporved=True)
