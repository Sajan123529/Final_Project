from django.shortcuts import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect


def rattsoffer(request):
    return render(request, "rattsoffers.html")
