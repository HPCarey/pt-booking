from django.shortcuts import render
from django.views import generic
from django.views import View
from .models import BookAppointment


class LandingPageView(View):
    model = BookAppointment
    template_name = 'index.html'
    
    def get(self, request):
        return render(request, "index.html")




# class UserBookingView(generic.FormView):
#     model = BookAppointment
#     form_class = BookingForm
#     template_name = 'create_booking_form.html'


# class UserProfileView(View):
#     model = BookAppointment
#     template_name = 'user_profile.html'


# class ChangeBookingView(generic.FormView):
#     model = BookAppointment
#     template_name = 'change_boooking_form.html'
