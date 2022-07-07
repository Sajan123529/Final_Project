from django.db import models

class rattsoffer(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=500)
    detials = models.TextField(max_length=5000)


class packagedetails(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    details = models.TextField(max_length=5000)
    photo = models.ImageField()