from django.shortcuts import render, redirect
from .models import HotelRoomsModel, Booking
import calendar
from datetime import timedelta, datetime
from django.http import HttpResponse
from .forms import BookingForm
import json

# Create your views here.
def home_view(request):
    rooms = HotelRoomsModel.objects.all()
    context = {
        "rooms" : rooms
    }
    return render(request, "index.html", context)

def room_detail_view(request, slug):
    room = HotelRoomsModel.objects.get(slug = slug)

    # check availability
    bookings = Booking.objects.filter(room = room)
    unavailable_dates = []

    for booking in bookings :
        current_date = booking.check_in
        while current_date <= booking.check_out:
            unavailable_dates.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

    context = {
        "room" : room,
        "unavailable_days" : unavailable_dates,
    }
    return render(request, "hotel-detail.html", context)




def booking_view(request, id):
    check_in = request.GET.get("check_in")
    check_out = request.GET.get("check_out")

    check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
    check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()

    room = HotelRoomsModel.objects.get(id=id)

    total_night = (check_out_date - check_in_date).days 

    total_days = total_night + 1

    room_price = room.room_price

    total_price = room_price * total_night

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = Booking.objects.create(
                room = room,
                check_in = check_in,
                check_out = check_out,
                amount = total_price,
                guest_name = form.cleaned_data["guest_name"],
                guest_email = form.cleaned_data["guest_email"],
                guest_phone = form.cleaned_data["guest_phone"]
            )

            return redirect("home")
    else:
        form = BookingForm()

    context = {
        "room" : room,
        "check_in" : check_in,
        "check_out" : check_out,
        "form" : form,
        "room_price" : room_price,
        "total_price" : total_price,
        "total_night" : total_night,
        "total_days" : total_days,

    }
    return render(request, "booking.html", context)