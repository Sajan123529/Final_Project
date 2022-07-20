from django.db import models
from django.conf import settings
from sqlite3 import *
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


# Create your models here.


class RoomCategory(models.Model):
    Room_Category = models.CharField(max_length=50)
    Rate = models.FloatField()
    Description = models.TextField(max_length=2000, null=False)

    def __str__(self):
        return self.Room_Category


class RoomTypefield(models.Model):
    name = models.CharField(max_length=100)
    Rate = models.IntegerField()

    def __str__(self):
        return self.name


class BedTypefield(models.Model):
    name = models.CharField(max_length=100)
    Rate = models.IntegerField()

    def __str__(self):
        return self.name


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

# Room_choice = (
#     ("with bathroom", "with bathroom"),
#     ("without bathroom", "without bathroom"),
#     ("deluxe room", "deluxe room"),
#     ("super deluxe room", "super deluxe room"),
#     ("normal room", "normal room"),
# )

Choose_Hotel_choice = (
    ("Annapurna", "Annapurna"),
    ("Kumar Hotel", "Kumar Hotel"),
    ("Hotel A One", "Hotel A One"),
    ("Family Resort", "Family Resort"),
    ("Dhulikhel Valley Resort", "Dhulikhel Valley Resort"),
    ("Dakshinkali Home Stay-OYO", "Dakshinkali Home Stay-OYO"),
    ("Bhaktapur Valley View Resort", "Bhaktapur Valley View Resort"),
    ("Panauti Hotel", "Panauti Hotel"),
    ("KU Home Stay", "KU Home Stay"),
    ("Devithan Valley Resort", "Devithan Valley Resort"),
    ("Chandeswori Home Stay-OYO", "Chandeswori Home Stay-OYO"),
    ("Kavre-Bhaktapur Valley Resort", "Kavre-Bhaktapur Valley Resort"),
    ("Ra.Ts Valley Resort", "Ra.Ts Valley Resort"),
)


# Bed_choice = (
#     ("Queen Size Bed", "Queen Size Bed"),
#     ("Deluxe Bed", "Deluxe Bed"),
#     ("Normal Bed", "Normal Bed"),
#     ("Double Bed", "Double Bed"),
#     ("Single Bed", "Single Bed"),
# )


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
    Adult = models.CharField(max_length=100, choices=Adult_choice, null=True, blank=True)
    Children = models.CharField(max_length=100, choices=Children_choice, null=True, blank=True)
    Destination_Hotel = models.CharField(choices=Destination_Hotel_choice, max_length=100, null=True, blank=True)
    Room_Type = models.ForeignKey(RoomTypefield, on_delete=models.CASCADE, null=True, blank=True)
    Choose_Hotel = models.CharField(max_length=100, choices=Choose_Hotel_choice)
    Bed_type = models.ForeignKey(BedTypefield, on_delete=models.CASCADE, null=True, blank=True)
    Rate = models.FloatField(max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Name


@receiver(post_save, sender=RoomBooking)
def Price(sender, instance, created, *args, **Kwargs):
    rate = instance.Rate
    print(instance.Rate,":::::::::::Instance:::::::::::::;;;")
    rate.save()
