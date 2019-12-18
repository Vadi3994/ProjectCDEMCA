from django.db import models

# Create your models here   
    
class PropertyDetails(models.Model):
    PropertyName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    AgentName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Availability = models.CharField(max_length=100)
    PropertyType = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Bed = models.CharField(max_length=100)
    Bath = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    Pool = models.CharField(max_length=100)
    DimView = models.CharField(max_length=100)
    Furnished = models.CharField(max_length=100)
    
    def __str__(self):
        return '%s' % (self.PropertyName)
    