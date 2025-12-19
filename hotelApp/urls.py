from django.urls import path
from .views import *

urlpatterns = [
   path('', home_view, name='home'),
   path('room/<str:slug>/', room_detail_view, name='room-detail'),
   # path('available/<int:id>/', room_availability, name='room-availability'),
   path('booking/<int:id>/', booking_view, name='booking'),
   path('initiate-payment/<int:id>/', initiate_payment, name="initiate-payment" ),
   path('payment-success/', success_view, name="payment-success" ),
   path('payment-failed/', failure_view, name="payment-failed" ),
   path('payement/callback', payment_callback, name="payment_callback")
   
]
