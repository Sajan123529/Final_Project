from django.db import models
from django.conf import settings
# Create your models here.


class RoomCat(models.Model):
    Room_Category = models.CharField(max_length=50)
    Rate = models.FloatField()
    Description = models.TextField(max_length=2000, null=False)

    def __str__(self):
        return self.Room_Category


class Room(models.Model):
    Name = models.CharField()
    Email = models.CharField()
    Phone = models.IntegerField()
    District = models.CharField()
    city = models.CharField()
    Street = models.CharField()
    Emergency_Phone = models.IntegerField()
    Country = models.CharField()
    Arrive_Date = models.DateTimeField()
    Depart_Date = models.DateTimeField()
    Adult = models.CharField()
    Children = models.CharField()
    Destination_Hotel = models.CharField()
    Room_Type = models.CharField()
    Choose_Hotel = models.CharField()
    Bed_Type = models.CharField()
    Description = models.TextField(max_length=2000, null=False)
    Category = models.ForeignKey(RoomCat, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Name


class Booking(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room)
    Arrive_Date = models.DateTimeField()
    Depart_Date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked From = {self.Arrive_Date.strftime("%d-%b-%Y %H:%M")} To = {self.Depart_Date.strftime("%d-%b-%Y %H:%M")}{self.room}'


class FlightCat(models.Model):
    Category = models.CharField(max_length=50)
    Rate = models.FloatField()
    Description = models.TextField(max_length=2000, null=False)

    def __str__(self):
        return self.Category


class flighttype(models.Model):
    One_Way = models.CharField()
    Two_Way= models.CharField()


class Flight(models.Model):
    Name = models.CharField()
    Email = models.CharField()
    Phone = models.IntegerField()
    District = models.CharField()
    city = models.CharField()
    Street = models.CharField()
    Emergency_Phone = models.IntegerField()
    Country = models.CharField()
    Departure_Date = models.DateTimeField()
    Landing_Date = models.DateTimeField()
    Adult = models.CharField()
    Children = models.CharField()
    Departure_Airport = models.CharField()
    Ticket_Type = models.CharField()
    Landing_Airport = models.CharField()
    Description = models.TextField(max_length=2000, null=False)
    Category = models.ForeignKey(FlightCat, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Name


class FlightBooking(models.Model):
    User = models.ForeignKey(User=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE))
    Flight = models.ForeignKey(Flight)
    Departure_Date = models.DateTimeField()
    Landing_Date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked From = {self.Arrive_Date.strftime("%d-%b-%Y %H:%M")} To = {self.Depart_Date.strftime("%d-%b-%Y %H:%M")}'


