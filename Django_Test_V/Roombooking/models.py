from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from sqlite3 import *


# Create your models here.


class RoomCategory(models.Model):
    Room_Category = models.CharField(max_length=50)
    Rate = models.FloatField()
    Description = models.TextField(max_length=2000, null=False)

    def __str__(self):
        return self.Room_Category


class RoomBooking(models.Model):
    Adult = (
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
    )

    Children = (
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
    )

    Destination_Hotel = (
        ("kathmandu", "kathmandu"),
        ("bhaktapur", "bhaktapur"),
        ("sanga", "sanga"),
        ("banepa", "banepa"),
        ("dhulikhel", "dhulikhel"),
        ("panauti", "panauti"),
    )

    Room_Type = (
        ("with bathroom", "with bathroom"),
        ("without bathroom", "without bathroom"),
        ("deluxe room", "deluxe room"),
        ("super deluxe room", "super deluxe room"),
        ("normal room", "normal room"),
    )

    Choose_Hotel = (
        ("abc", "abc"),
        ("bcd", "bcd"),
        ("efg", "efg"),
        ("ghi", "ghi"),
        ("jkl", "jkl"),
    )

    Bed_Type = (
        ("abc", "abc"),
        ("bcd", "bcd"),
        ("efg", "efg"),
        ("ghi", "ghi"),
        ("jkl", "jkl"),
    )

    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    Phone = models.IntegerField()
    District = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    Emergency_Phone = models.IntegerField()
    Country = models.CharField(max_length=100)
    Arrive_Date = models.DateField(max_length=50)
    Depart_Date = models.DateField(max_length=50)
    Adult = models.CharField(max_length=50, choices=Adult)
    Children = models.CharField(max_length=50, choices=Children)
    Destination_Hotel = models.CharField(max_length=200, choices=Destination_Hotel)
    Room_Type = models.CharField(max_length=100, choices=Room_Type)
    Choose_Hotel = models.CharField(max_length=100, choices=Choose_Hotel)
    Bed_Type = models.CharField(max_length=100, choices=Bed_Type)
    Rate = models.FloatField(max_length=50)
    Description = models.TextField(max_length=2000, null=False)
    Category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Name


class Room_Book(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Room = models.ForeignKey(RoomBooking, on_delete=models.CASCADE)
    Arrive_Date = models.DateField()
    Depart_Date = models.DateField()

    def __str__(self):
        return f'{self.User} has booked From = {self.Arrive_Date("%d-%b-%Y")} To = {self.Depart_Date("%d-%b-%Y")}{self.Room}'
