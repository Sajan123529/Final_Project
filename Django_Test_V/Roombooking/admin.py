from django.apps import AppConfig
from django.contrib import admin
from .models import RoomBooking, RoomCategory

admin.site.register(RoomBooking),
admin.site.register(RoomCategory),
