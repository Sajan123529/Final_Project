from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path('rattsoffer/', views.rattsoffer, name='rattsoffer'),
]