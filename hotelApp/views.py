from django.shortcuts import render
from .models import *
# Create your views here.

def home_view(request):
    rooms = HotelRoomsModel.objects.all()
    context = {
        "rooms" : rooms
    }
    return render(request, "homepage.html", context)

def room_detail_view(request, id):
    room = HotelRoomsModel.objects.get(id = id)