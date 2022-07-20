from django.apps import AppConfig
from django.contrib import admin
from .models import RoomBooking, RoomCategory, RoomTypefield, BedTypefield

admin.site.register(RoomBooking),
admin.site.register(RoomCategory),
admin.site.register(RoomTypefield),
admin.site.register(BedTypefield),


