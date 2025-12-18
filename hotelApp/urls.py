from django.urls import path
from .views import *

urlpatterns = [
   path('', home_view, name='home'),
   path('room/<str:slug>/', room_detail_view, name='room-detail'),
   # path('available/<int:id>/', room_availability, name='room-availability'),
   path('booking/<int:id>/', booking_view, name='booking'),
]
