from django.db import models

# Create your models here.
class OurPartners(models.Model):
    Parntername = models.CharField(max_length=50)
    Logo = models.ImageField()


class OurDailyPosts(models.Model):
    PlaceName = models.CharField(max_length=50)
    Descriptoon = models.TextField(max_length=2000)
    Photo = models.ImageField()