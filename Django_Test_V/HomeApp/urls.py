from django.urls import path
from HomeApp.views import *
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path('home/', views.LandingPage_View, name='homepage'),
]