from django.db import models

class rattsoffer(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=500)
    detials = models.CharField(max_length=5000)