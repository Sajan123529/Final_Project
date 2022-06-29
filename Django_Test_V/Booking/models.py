from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class RoomCat(models.Model):
    Room_Category = models.CharField(max_length=50)
    Rate = models.FloatField()
    Description = models.TextField(max_length=2000, null=False)

    def __str__(self):
        return self.Room_Category


class Room(models.Model):
    Adult = (
        ("", ""),
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
    )

    Children=(
        ("", ""),
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
    )

    Destination_Hotel=(
        ("", ""),
        ("kathmandu", "kathmandu"),
        ("bhaktapur", "bhaktapur"),
        ("sanga", "sanga"),
        ("banepa", "banepa"),
        ("dhulikhel", "dhulikhel"),
        ("panauti", "panauti"),
    )

    Room_Type=(
        ("", ""),
        ("with bathroom", "with bathroom"),
        ("without bathroom", "without bathroom"),
        ("deluxe room", "deluxe room"),
        ("super deluxe room", "super deluxe room"),
        ("normal room", "normal room"),
    )

    Choose_Hotel=(
        ("", ""),
        ("abc", "abc"),
        ("bcd", "bcd"),
        ("efg", "efg"),
        ("ghi", "ghi"),
        ("jkl", "jkl"),
    )

    Bed_Type=(
        ("", ""),
        ("abc", "abc"),
        ("bcd", "bcd"),
        ("efg", "efg"),
        ("ghi", "ghi"),
        ("jkl", "jkl"),
    )

    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    Phone = models.IntegerField(max_length=50)
    District = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    Emergency_Phone = models.IntegerField(max_length=50)
    Country = models.CharField(max_length=100)
    Arrive_Date = models.DateTimeField(max_length=50)
    Depart_Date = models.DateTimeField(max_length=50)
    Adult = models.CharField(max_length=50, choices=Adult)
    Children = models.CharField(max_length=50, choices=Children)
    Destination_Hotel = models.CharField(max_length=200, choices=Destination_Hotel)
    Room_Type = models.CharField(max_length=100, choices=Room_Type)
    Choose_Hotel = models.CharField(max_length=100, choices=Choose_Hotel)
    Bed_Type = models.CharField(max_length=100, choices=Bed_Type)
    Description = models.TextField(max_length=2000, null=False)
    Category = models.ForeignKey(RoomCat, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Name


class Booking(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
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


class FlightType(models.Model):
    One_Way = models.CharField(max_length=50, null=False)
    Two_Way= models.CharField(max_length=50, null=False)


class Flight(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    Phone = models.IntegerField(max_length=50)
    District = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    Emergency_Phone = models.IntegerField(max_length=50)
    Country = models.CharField(max_length=100)
    Departure_Date = models.DateTimeField(max_length=50)
    Landing_Date = models.DateTimeField(max_length=50)
    Adult = models.CharField(max_length=50)
    Children = models.CharField(max_length=50)
    Departure_Airport = models.CharField(max_length=50)
    Ticket_Type = models.CharField(max_length=50)
    Landing_Airport = models.CharField(max_length=50)
    Description = models.TextField(max_length=2000, null=False)
    Category = models.ForeignKey(FlightCat, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Name


class FlightBook(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    Departure_Date = models.DateTimeField()
    Landing_Date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked From = {self.Arrive_Date.strftime("%d-%b-%Y %H:%M")} To = {self.Depart_Date.strftime("%d-%b-%Y %H:%M")}'


