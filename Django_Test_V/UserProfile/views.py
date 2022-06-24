from django.urls import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
# Create your views here.


@login_required(login_url="/login/")
def User_View(request):
    return render(request,"userprofile.html")