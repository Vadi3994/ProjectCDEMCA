from django.db import models

# Create your models here   

class Agent(models.Model):
    AgentName = models.CharField(max_length=100, default="")
    Password = models.CharField(max_length=100, default="")
    PhoneNumber = models.CharField(max_length=100, default="")
    Gender = models.CharField(max_length=100, default="")
    Email = models.CharField(max_length=100, default="")
    PropPublished = models.CharField(max_length=100, default="")
    Sold = models.CharField(max_length=100, default="")
    ProfileStat = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return '%s' % (self.AgentName)
    
class PropertyDetails(models.Model):
    PropertyName = models.CharField(max_length=100, default="")
    Address = models.CharField(max_length=100, default="")
    Location = models.CharField(max_length=100, default="")
    PhoneNumber = models.CharField(max_length=100, default="")
    AgentName = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    Email = models.CharField(max_length=100, default="")
    Availability = models.CharField(max_length=100, default="")
    PropertyType = models.CharField(max_length=100, default="")
    Price = models.CharField(max_length=100, default="")
    Bed = models.CharField(max_length=100, default="")
    Bath = models.CharField(max_length=100, default="")
    Area = models.CharField(max_length=100, default="")
    Pool = models.CharField(max_length=100, default="")
    DimView = models.CharField(max_length=100, default="")
    Furnished = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return '%s' % (self.PropertyName)
  
    
class Customer(models.Model):
    CustomerName = models.CharField(max_length=100, default="")
    Password = models.CharField(max_length=100, default="")
    Gender = models.CharField(max_length=100, default="")
    PhoneNumber = models.CharField(max_length=100, default="")
    Email = models.CharField(max_length=100, default="")
    Age = models.CharField(max_length=100, default="")
    Location = models.CharField(max_length=100, default="")
    Bought = models.CharField(max_length=100, default="")
    ProfileStat = models.CharField(max_length=100, default="")
    LastLogin = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return '%s' % (self.CustomerName)
    
class PropertiesSold(models.Model):
    Property = models.CharField(max_length=100, default="")
    PropID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    AgentName = models.CharField(max_length=100, default="")
    CustomerName = models.CharField(max_length=100, default="")
    Location = models.CharField(max_length=100, default="")
    DateOfSale = models.CharField(max_length=100, default="")
    Email = models.DateField(max_length=100, default="")
    
    def __str__(self):
        return '%s' % (self.Property)