from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .forms import AvailabilityForm, RoomForm
from .models import *


# Create your views here.

# @login_required(login_url="/login/")
def BookingPage_view_create_view(request):
    if request.method == "POST":
        print(":::::::::::::::::POST::::::::::::::::::::::::::::::::::::::::::")
        form = RoomForm(request.POST)
        if form.is_valid():
            print("::::::::::::::::::::Form valid:::::::::::::::::::::::::::::::::::::::")
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Phone = form.cleaned_data['Phone']
            District = form.cleaned_data['Phone']
            city = form.cleaned_data['city']
            Street = form.cleaned_data['Street']
            Emergency_Phone = form.cleaned_data['Emergency_Phone']
            Country = form.cleaned_data['Country']
            Arrive_Date = form.cleaned_data['Arrive_Date']
            Depart_Date = form.cleaned_data['Depart_Date']
            Adult = form.cleaned_data['Adult']
            Children = form.cleaned_data['Children']
            Destination_Hotel = form.cleaned_data['Destination_Hotel']
            Room_Type = form.cleaned_data['Room_Type']
            print(Room_Type,":::::::::::::::::::::::::::::::::::")
            Choose_Hotel = form.cleaned_data['Choose_Hotel']
            Bed_type = form.cleaned_data['Bed_type']
            Rate = form.cleaned_data['Rate']
            Description = form.cleaned_data['Description']

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
                Bed_type=Bed_type,
                Rate=Rate,
                Description=Description
            )
            Roombooking.save()
            messages.success(request, ('Asset Account was created successfully.'))
            return redirect(reverse('room-booking:booking'))
        else:
            print("Error Occured::: ", form.errors)
            context = {
                'form': form,
                'Adult_choice': Adult_choice,
                'Children_choice': Children_choice,
                'Destination_Hotel_choice': Destination_Hotel_choice,
                'Room_Type': RoomTypefield.objects.all(),
                'Choose_Hotel_choice': Choose_Hotel_choice,
                'Bed_type': BedTypefield.objects.all(),
            }
            return render(request, 'roombooking.html', context, {'form': form})
    else:
        form = RoomForm()
        context = {
            'form': form,
            'Adult_choice': Adult_choice,
            'Children_choice': Children_choice,
            'Destination_Hotel_choice': Destination_Hotel_choice,
            'Room_Type': RoomTypefield.objects.all(),
            'Choose_Hotel_choice': Choose_Hotel_choice,
            'Bed_type': BedTypefield.objects.all(),
        }
        return render(request, 'roombooking.html', context)



