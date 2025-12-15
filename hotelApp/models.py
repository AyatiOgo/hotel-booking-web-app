from django.db import models
from autoslug import AutoSlugField

# Create your models here.
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
    
class Booking(models.Model):
    room = models.ForeignKey(HotelRoomsModel, related_name="bookings", on_delete=models.CASCADE )
    check_in = models.DateField(max_length=50)
    check_out = models.DateField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_number = models.CharField(max_length=20)