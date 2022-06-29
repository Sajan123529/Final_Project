from django import forms
from datetime import datetime
from .models import RoomCat


class AvailabilityForm(forms.Form):
    Arrive_Date = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    Depart_Date = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


Adult =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class AdultForm(forms.Form):
    adult_field = forms.ChoiceField(choices=Adult)


Children=(
    ("", ""),
    ("1", "one"),
    ("2", "two"),
    ("3", "three"),
    ("4", "four"),
    ("5", "five"),
)

class ChildrenForm(forms.Form):
    adult_field = forms.ChoiceField(choices=Children)

Destination_Hotel=(
    ("", ""),
    ("kathmandu", "kathmandu"),
    ("bhaktapur", "bhaktapur"),
    ("sanga", "sanga"),
    ("banepa", "banepa"),
    ("dhulikhel", "dhulikhel"),
    ("panauti", "panauti"),
)

class DestinationHotelForm(forms.Form):
    adult_field = forms.ChoiceField(choices=Destination_Hotel)

Room_Type=(
    ("", ""),
    ("with bathroom", "with bathroom"),
    ("without bathroom", "without bathroom"),
    ("deluxe room", "deluxe room"),
    ("super deluxe room", "super deluxe room"),
    ("normal room", "normal room"),
)

class RoomTypeForm(forms.Form):
    adult_field = forms.ChoiceField(choices=Room_Type)

Choose_Hotel=(
    ("", ""),
    ("abc", "abc"),
    ("bcd", "bcd"),
    ("efg", "efg"),
    ("ghi", "ghi"),
    ("jkl", "jkl"),
)

class ChooseHotelForm(forms.Form):
    adult_field = forms.ChoiceField(choices=Choose_Hotel)

Bed_Type = (
    ("", ""),
    ("abc", "abc"),
    ("bcd", "bcd"),
    ("efg", "efg"),
    ("ghi", "ghi"),
    ("jkl", "jkl"),
)

class BedTypeForm(forms.Form):
    adult_field = forms.ChoiceField(choices=Bed_Type)