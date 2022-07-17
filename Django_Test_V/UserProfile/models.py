from django.db import models

class userprofile(models.Model):
    Productname = models.CharField(max_length=200)
    Price = models.FloatField(max_length=50)
    Image = models.ImageField()
