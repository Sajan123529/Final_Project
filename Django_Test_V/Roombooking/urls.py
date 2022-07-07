from django.urls import path
from HomeApp.views import *
from . import views
from django.urls import include, re_path

app_name = 'room-booking'

urlpatterns = [
    re_path('booking/', views.BookingPage_view_create_view, name='booking'),
]