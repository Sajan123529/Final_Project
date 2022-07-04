from django import forms
from datetime import datetime
from .models import RoomCategory
from .models import RoomBooking
from sqlite3 import *


class RoomForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = "__all__"
        exclude = []




class AvailabilityForm(forms.Form):
    Arrive_Date = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", "%Y-%m-%d"], widget=forms.DateInput(attrs={'type': 'date-local'}))
    Depart_Date = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", "%Y-%m-%d"], widget=forms.DateInput(attrs={'type': 'date-local'}))

