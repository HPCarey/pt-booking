from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.views import generic
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import BookAppointment
from .forms import AddBooking, UpdateBooking


def index(request):
    return render(request, "index.html")


@login_required
def add_booking(request):
    if request.method == 'POST':
        booking = BookAppointment(user=request.user)
        form = AddBooking(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = AddBooking()
    return render(request, 'add_booking.html', {'form': form})


@login_required
def user_profile(request):
    user = request.user
    bookings = BookAppointment.objects.filter(user=user)
    return render(request, 'user_profile.html', {
        'user': user,
        'bookings': bookings,
    })


@login_required
def update_booking(request, id):
    if request.method == 'POST':
        booking = get_object_or_404(BookAppointment, pk=id, user=request.user)
        form = UpdateBooking(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UpdateBooking()
    context = {
        'form': form,
    }
    return render(request, 'update_booking.html', context)


@login_required
def delete_booking(request, id):
    booking = get_object_or_404(BookAppointment, pk=id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('user_profile')
    return render(request, 'delete_booking.html', {
        'booking': booking,
    })

   # booking = get_object_or_404(BookAppointment, pk=id, user=request.user)
    # if request.method == 'GET':
    #     context = {'form': AddBooking(instance=booking), 'id': id}
    #     return render(request, 'add_form', context)re