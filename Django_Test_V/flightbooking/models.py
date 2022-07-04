from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


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
    Phone = models.IntegerField()
    District = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    Emergency_Phone = models.IntegerField()
    Country = models.CharField(max_length=100)
    Departure_Date = models.DateField(max_length=50)
    Landing_Date = models.DateField(max_length=50)
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
    Departure_Date = models.DateField()
    Landing_Date = models.DateField()

    def __str__(self):
        return f'{self.user} has booked From = {self.Arrive_Date("%d-%b-%Y")} To = {self.Depart_Date("%d-%b-%Y")}'



