from django.shortcuts import render, redirect
from .models import HotelRoomsModel, Booking
import calendar
from datetime import timedelta, datetime
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
def home_view(request):
    rooms = HotelRoomsModel.objects.all()
    context = {
        "rooms" : rooms
    }
    return render(request, "index.html", context)

def room_detail_view(request, slug):
    room = HotelRoomsModel.objects.get(slug = slug)
    context = {
        "room" : room
    }
    return render(request, "hotel-detail.html", context)

def room_availability(request, id):
    year = int(request.GET.get)
    month = int(request.GET.get)
    room = HotelRoomsModel.objects.get(id=id)
    bookings = Booking.objects.filter(
        room = room, 
        check_in__month__lte = month,
        check_out__month__gte = month
    )
    unavailable_dates = set()

    for booking in bookings :
        current_date = booking.check_in
        while current_date <= booking.check_out:
            unavailable_dates.add(current_date.isoformat())
            current_date += timedelta(days=1)

    return HttpResponse({
        "days" : list(unavailable_dates) 
    })


def booking_view(request, id):
    check_in = request.GET.get("check_in")
    check_out = request.GET.get("check_out")

    check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
    check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()

    room = HotelRoomsModel.objects.get(id=id)

    total_night = (check_out_date - check_in_date).days 

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
    }
    return render(request, "booking.html", context)