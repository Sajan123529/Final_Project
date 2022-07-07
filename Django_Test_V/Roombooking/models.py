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

Adult_choice = (
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
    )
Children_choice = (
    ("1", "one"),
    ("2", "two"),
    ("3", "three"),
    ("4", "four"),
    ("5", "five"),
)

Destination_Hotel_choice = (
    ("kathmandu", "kathmandu"),
    ("bhaktapur", "bhaktapur"),
    ("sanga", "sanga"),
    ("banepa", "banepa"),
    ("dhulikhel", "dhulikhel"),
    ("panauti", "panauti"),
)

Room_choice = (
    ("with bathroom", "with bathroom"),
    ("without bathroom", "without bathroom"),
    ("deluxe room", "deluxe room"),
    ("super deluxe room", "super deluxe room"),
    ("normal room", "normal room"),
)

Choose_Hotel_choice = (
    ("abc", "abc"),
    ("bcd", "bcd"),
    ("efg", "efg"),
    ("ghi", "ghi"),
    ("jkl", "jkl"),
)

Bed_choice = (
    ("abc", "abc"),
    ("bcd", "bcd"),
    ("efg", "efg"),
    ("ghi", "ghi"),
    ("jkl", "jkl"),
)

class RoomBooking(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField()
    District = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    Street = models.CharField(max_length=100, null=True, blank=True)
    Emergency_Phone = models.IntegerField()
    Country = models.CharField(max_length=100, null=True, blank=True)
    Arrive_Date = models.DateField(max_length=100, null=True, blank=True)
    Depart_Date = models.DateField(max_length=100, null=True, blank=True)
    Adult = models.CharField(max_length=15, choices = Adult_choice)
    Children = models.CharField(max_length=15, choices = Children_choice)
    Destination_Hotel = models.CharField(max_length=100, choices = Destination_Hotel_choice)
    Room_Type = models.CharField(max_length=100, choices = Room_choice)
    Choose_Hotel = models.CharField(max_length=100, choices = Choose_Hotel_choice)
    Bed_type = models.CharField(max_length=15, choices = Bed_choice)
    Rate = models.FloatField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Name


