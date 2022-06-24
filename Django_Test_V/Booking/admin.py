from django.apps import AppConfig
from django.contrib import admin
from .models import Room, RoomCat, Booking, FlightCat, FlightType, FlightBook

admin.site.register(Room),
admin.site.register(RoomCat),
admin.site.register(Booking),
admin.site.register(FlightCat),
admin.site.register(FlightType),
admin.site.register(FlightBook)
