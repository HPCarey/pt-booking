from django.contrib import admin
from .models import BookAppointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BookAppointment)
class AppointmentAdmin(SummernoteModelAdmin):
    """
    Customise the django admin panel for superuser
    Adds features for site user to organise bookings
    Search filter by client name
    Summernote fields for longer content
    Ability to apprive bookings
    """
    list_display = (
        'first_name', 'last_name', 'date', 'time', 'created_on',
        'updated_on'
    )
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ('first_name', 'last_name', 'email', 'date')
    summernote_fields = ('goals', 'health_info')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(apporved=True)
