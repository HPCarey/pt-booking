from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.views import generic
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import BookAppointment
from .forms import AddBooking, UpdateBooking


def index(request):
    """
    Renders the index page
    """
    return render(request, "index.html")


def error_404(request, exception):
    """
    Renders the custom 404 page for the app
    """
    return render(request, 'booking/404.html')


@login_required
def add_booking(request):
    """
    Handle the "create" functionality for bookings.
    Render the booking form.
    If request is POST, check that inputs are valid.
    Display error message for duplicate bookings,
    dates in the past and incorrect user input.
    If form is valid and no duplicates, save
    the booking and redirect to user's profile

    """
    if request.method == 'POST':
        booking = BookAppointment(user=request.user)
        form = AddBooking(request.POST, instance=booking)
        if form.is_valid():
            if not BookAppointment.objects.filter(
                    user=request.user,
                    date=booking.date).exists():
                form.save()
                messages.success(request, 'Booking added successfully.')
                return redirect('user_profile')
            else:
                messages.error(
                    request,
                    'Duplicate booking. Please choose a different date'
                    )
        else:
            messages.error(
                request, 'Invalid form data. Please check the entered values.')
    else:
        form = AddBooking()
    return render(request, 'add_booking.html', {'form': form})


@login_required
def user_profile(request):
    """
    Allow logged in user to view their appointments
    Fetch all bookings associated with the logged-in user
    and render them on the user profile page.
    """
    user = request.user
    bookings = BookAppointment.objects.filter(user=user)
    return render(request, 'user_profile.html', {
        'user': user,
        'bookings': bookings,
    })


@login_required
def update_booking(request, id):
    """
    Handle the Edit functionality for bookings
    Render the update booking form pre-populated
    with the existing booking details.
    If request is POST, check that inputs are valid.
    Display error message for duplicate bookings,
    dates in the past and incorrect user input.
    Exclude the current booking date from duplicate bookings
    to allow user to keep the original date.
    If the form valid no duplicates,
    save the changes and redirect to the user's profile page.

    """
    booking = get_object_or_404(BookAppointment, pk=id, user=request.user)
    if request.method == 'POST':
        form = UpdateBooking(request.POST, instance=booking)
        if form.is_valid():
            if not BookAppointment.objects.filter(
                    user=request.user,
                    date=booking.date).exclude(pk=id).exists():
                form.save()
                messages.success(request, 'Booking updated successfully.')
                return redirect('user_profile')
            else:
                messages.error(
                    request,
                    'Duplicate booking.Please choose a different date'
                )
        else:
            messages.error(
                request, 'Invalid form data. Please check the entered values.')
    else:
        form = UpdateBooking(instance=booking)
    context = {
        'form': form,
    }
    return render(request, 'update_booking.html', context)


@login_required
def delete_booking(request, id):
    """
    Handle the Delete functionality of a booking
    Render the confirmation page for deleting the booking.
    Delete the booking from the database
    and redirect to the user's profile page.
    Display a success message to confirm deletion
    """
    booking = get_object_or_404(BookAppointment, pk=id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('user_profile')
    return render(request, 'delete_booking.html', {
        'booking': booking,
    })
