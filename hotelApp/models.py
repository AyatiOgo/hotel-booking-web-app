from django.db import models
from autoslug import AutoSlugField
import uuid
from django.contrib.auth.models import AbstractUser
from booking.settings import AUTH_USER_MODEL
# Create your models here.


class HotelUsers(AbstractUser):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=50, unique=True)
    phone_no = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class HotelRoomsModel(models.Model):
    room_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='room_name', null=True, blank=True)
    room_image = models.ImageField(null=True, blank=True)
    room_description = models.TextField(max_length=2000)
    room_no = models.IntegerField()
    room_price = models.IntegerField()
    room_dimension = models.CharField(max_length=50)
    room_bed_no = models.CharField(max_length=50)
    room_occupants_no = models.CharField(max_length=100)
    room_meal_access = models.CharField(max_length=100)
    room_electricity = models.BooleanField(default=True)
    room_AC = models.BooleanField(default=True)
    room_pool_access = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name
    

class RoomImages(models.Model):
    room = models.ForeignKey(HotelRoomsModel, related_name="images", on_delete=models.CASCADE )
    images = models.ImageField()


STATUS_CHOICES = [
    ("pending", "pending"),
    ("confirmed", "confirmed"),
    ("failed", "failed"),
]

class Booking(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(HotelRoomsModel, related_name="bookings", on_delete=models.CASCADE )
    check_in = models.DateField(max_length=50)
    check_out = models.DateField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=20)
    booking_ref = models.CharField(max_length=20, unique=True, blank=True, null=True )
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, null=True, blank=True, default="pending")
    payment_refrence = models.CharField(max_length=100, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.booking_ref:
            self.booking_ref = f"BK{uuid.uuid4().hex[:6].upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.booking_ref
    

