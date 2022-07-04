from django.shortcuts import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from . import models
 #Create your views here.


def LandingPage_View(request):
    current = datetime.now()
    return render(request,"homepage.html")