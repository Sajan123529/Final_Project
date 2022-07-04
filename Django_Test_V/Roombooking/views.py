from django.contrib import messages
from django.urls import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import RoomBooking
from .models import RoomBooking
from .forms import RoomForm
from sqlite3 import *
import sqlite3

# Create your views here.


# def BookingPage_View(request):
#     #form_class = AvailabilityForm
#     return render(request,"roombooking.html")
#     return render(request,"flightbooking.html")


con = sqlite3.connect("db.sqlite3")

@login_required(login_url="/login/")
def BookingPage_view_create_view(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data('Name')
            Email = form.cleaned_data('Email')
            Phone = form.cleaned_data('Phone')
            District = form.cleaned_data('Phone')
            city = form.cleaned_data('city')
            Street = form.cleaned_data('Street')
            Emergency_Phone = form.cleaned_data('Emergency_Phone')
            Country = form.cleaned_data('Country')
            Arrive_Date = form.cleaned_data('Arrive_Date')
            Depart_Date = form.cleaned_data('Depart_Date')
            Adult = form.cleaned_data('Adult')
            Children = form.cleaned_data('Children')
            Destination_Hotel = form.cleaned_data('Destination_Hotel')
            Room_Type = form.cleaned_data('Room_Type')
            Choose_Hotel = form.cleaned_data('Choose_Hotel')
            Bed_Type = form.cleaned_data('Bed_Type')
            Rate = form.cleaned_data('Rate')
            Description = form.cleaned_data('Description')
            Roombooking = RoomBooking.objects.create(
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
                Rate=Rate,
                Description=Description
            )
            RoomBooking.save()
            messages.success(request, ('Asset Account was created successfully.'))
            return redirect(reverse('/'))
        else:
            print("Error Occured::: ", form.errors)
            return render(request, 'roombooking.html', {'form': form})
    else:
        form = RoomForm()

    form = RoomBooking.objects.all()
    context = {'form': form}
    return render(request, 'roombooking.html', {'form': form})
