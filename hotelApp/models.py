from django.db import models

# Create your models here.
class HotelRoomsModel(models.Model):
    room_name = models.CharField(max_length=100)
    room_image = models.ImageField(null=True, blank=True)
    room_description = models.TextField(max_length=2000)
    room_no = models.IntegerField()
    room_price = models.IntegerField()

    def __str__(self):
        return self.room_name
    

class RoomImages(models.Model):
    room = models.ForeignKey(HotelRoomsModel, related_name="images", on_delete=models.CASCADE )
    images = models.ImageField()
    
class Booking(models.Model):
    room = models.ForeignKey(HotelRoomsModel, related_name="bookings", on_delete=models.CASCADE )
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_number = models.CharField(max_length=20)