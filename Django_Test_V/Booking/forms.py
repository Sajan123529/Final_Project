from django import forms
from datetime import datetime
from .models import RoomCat
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields= "__all__"


class AvailabilityForm(forms.Form):
    Arrive_Date = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", "%Y-%m-%d"], widget=forms.DateInput(attrs={'type': 'date-local'}))
    Depart_Date = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", "%Y-%m-%d"], widget=forms.DateInput(attrs={'type': 'date-local'}))

