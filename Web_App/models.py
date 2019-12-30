from django.db import models

# Create your models here   

class Agent(models.Model):
    AgentName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PropPublished = models.CharField(max_length=100)
    Sold = models.CharField(max_length=100)
    ProfileStat = models.CharField(max_length=100)
    
    def __str__(self):
        return '%s' % (self.AgentName)
    
class PropertyDetails(models.Model):
    PropertyName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    AgentName = models.ForeignKey(Agent, on_delete=models.CASCADE)
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
  
    
class Customer(models.Model):
    CustomerName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Bought = models.CharField(max_length=100)
    ProfileStat = models.CharField(max_length=100)
    LastLogin = models.CharField(max_length=100)
    
    def __str__(self):
        return '%s' % (self.CustomerName)
    
class PropertiesSold(models.Model):
    PropID = models.CharField(max_length=100)
    PropertyName = models.ForeignKey(PropertyDetails, on_delete=models.CASCADE)
    AgentName = models.ForeignKey(Agent, on_delete=models.CASCADE)
    CustomerName = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Location = models.CharField(max_length=100)
    DateOfSale = models.CharField(max_length=100)
    Email = models.DateField(max_length=100)
    
    def __str__(self):
        return '%s' % (self.PropID)