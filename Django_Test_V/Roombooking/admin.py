from django.apps import AppConfig
from django.contrib import admin
from .models import RoomBooking, RoomCategory, Room_Book

admin.site.register(RoomBooking),
admin.site.register(RoomCategory),
admin.site.register(Room_Book),
