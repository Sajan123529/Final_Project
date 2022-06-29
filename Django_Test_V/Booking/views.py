from django.contrib import messages
from django.urls import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Room
from .forms import AdultForm, ChildrenForm, DestinationHotelForm, RoomTypeForm, ChooseHotelForm, BedTypeForm


# Create your views here.


# def BookingPage_View(request):
#     #form_class = AvailabilityForm
#     return render(request,"roombooking.html")
#     return render(request,"flightbooking.html")


@login_required(login_url="/login/")
def BookingPage_view(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        District = request.POST.get('Phone')
        city = request.POST.get('city')
        Street = request.POST.get('Street')
        Emergency_Phone = request.POST.get('Emergency_Phone')
        Country = request.POST.get('Country')
        Arrive_Date = request.POST.get('Arrive_Date')
        Depart_Date = request.POST.get('Depart_Date')
        Adult = request.POST.get('Adult')
        Children = request.POST.get('Children')
        Destination_Hotel = request.POST.get('Destination_Hotel')
        Room_Type = request.POST.get('Room_Type')
        Choose_Hotel = request.POST.get('Choose_Hotel')
        Bed_Type = request.POST.get('Bed_Type')
        Description = request.POST.get('Description')

        context={}
        context['form']= AdultForm(), ChildrenForm(), DestinationHotelForm(), RoomTypeForm(), ChooseHotelForm(), BedTypeForm()

        bookingdata = Room(
            Name=Name,
            Email=Email,
            Phone=Phone,
            District=District,
            city=city,
            Street=Street,
            Emergency_Phone=Emergency_Phone,
            Country=Country,
            Arrive_Date=Arrive_Date,
            Depart_Date=Depart_Date,
            Adult=Adult,
            Children=Children,
            Destination_Hotel=Destination_Hotel,
            Room_Type=Room_Type,
            Choose_Hotel=Choose_Hotel,
            Bed_Type=Bed_Type,
            Description=Description
        )
        bookingdata.save()
        redirect('booking')

    return render(request, "roombooking.html")