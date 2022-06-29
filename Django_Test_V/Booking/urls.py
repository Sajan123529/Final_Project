from django.urls import path
from HomeApp.views import *
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path('booking/', views.BookingPage_view, name='booking'),
]
