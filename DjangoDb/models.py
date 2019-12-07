from django.db import models

# Create your models here.

class LocEvent(models.Model):
    propertyname = models.CharField('propertyname',max_length=10)
    Location = models.CharField('location',max_length=20)
    
    
class PropertyDetails(models.Model):
    PropertyName = models.CharField('PropertyName',max_length=100)
    Address = models.CharField('Address',max_length=100)
    Location = models.CharField('Location',max_length=100)
    PhoneNumber = models.CharField('PhoneNumber',max_length=100)
    AgentName = models.CharField('AgentName',max_length=100)
    Email = models.CharField('Email',max_length=100)
    Availability = models.CharField('Availability',max_length=100)
    PropertyType = models.CharField('PropertyType',max_length=100)