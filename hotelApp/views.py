from django.shortcuts import render, redirect
from .models import HotelRoomsModel, Booking
import calendar
from datetime import timedelta, datetime
from django.http import HttpResponse
from .forms import BookingForm
import json
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from booking.settings import PAYSTACK_SECRET_KEY
from django.urls import reverse


paystack = Paystack(secret_key=PAYSTACK_SECRET_KEY)

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

            return redirect("initiate-payment", id=booking.id)
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

def initiate_payment(request, id):
    booking = Booking.objects.get(id=id)

    # data = {
    #     "email" : booking.guest_email,
    #     "amount": int(booking.amount *100 ),
    #     "refrence": booking.booking_ref
    # }

    response = Transaction.initialize(email=booking.guest_email,
                                      amount= int(booking.amount *100 ),
                                      refrence = booking.booking_ref,
                                      callback_url = request.build_absolute_uri(reverse("payment_callback"))
                                      )


    booking.payment_refrence = response["data"]["reference"]
    booking.save()
    
    if response['status']:
        return redirect(response["data"]["authorization_url"])
    return HttpResponse("Initialization Failed", status=400)

def payment_callback(request):
    refrence = request.GET.get('reference')

    booking = Booking.objects.get(payment_refrence=refrence)
    response = paystack.transaction.verify(refrence)
    status = response['data']['status']

    if status == "success":
        booking.status = "confirmed"
        booking.save()
        return redirect("payment-success")

    else:
        booking.status = "failed"
        booking.save()
        return redirect("payment-failed")

def success_view(request):
    return render(request, "success.html")

def failure_view(request):
    return render(request, "success.html")