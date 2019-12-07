from django.db import models

# Create your models here.

class LocEvent(models.Model):
    propertyname = models.CharField('propertyname',max_length=10)
    Location = models.CharField('location',max_length=20)