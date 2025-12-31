from django.urls import path
from .views import *

urlpatterns = [
   path('', home_view, name='home'),
   path('room/<str:slug>/', room_detail_view, name='room-detail'),
   # path('available/<int:id>/', room_availability, name='room-availability'),
   path('booking/<int:id>/', booking_view, name='booking'),
   path('initiate-payment/<int:id>/', initiate_payment, name="initiate-payment" ),
   path('payment-success/<str:ref>', success_view, name="payment-success" ),
   path('payment-failed/', failure_view, name="payment-failed" ),
   path('payment/callback', payment_callback, name="payment_callback"),
   path('booking/download/', download_page, name="download_page"),
   path('create-account/', registration_view, name="create-account"),
   path('login/', loginUser_view, name="login"),
   path('logout/', logout_view, name="logout"),
   path('booking/check-booking/', find_booking_view, name="check-booking"),
   path('booking/details/<str:ref>', booking_details, name="booking-details"),
   
]
