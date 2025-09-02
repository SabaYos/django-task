from django.db import models

# Create your models here.

class Client (models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    number_stores = models.IntegerField()
    def __str__(self):
        return self.title
    
class Store (models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='stores')
    def __str__(self):
        return self.title
    
class Employee (models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    current_store = models.ForeignKey(Store,null=True, on_delete=models.SET_NULL, related_name="employees")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="employees")
    def __str__(self):
        return self.title
    
    