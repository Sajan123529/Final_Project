from django.urls import path
from UserLogReg.views import *
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path('login/', views.LoginView, name='login'),
    re_path('register/', views.RegisterView, name='register'),
    re_path('logout/', views.logout_View, name='logout'),
]
