from django.db import models

# Create your models here.

class Car(models.Model): # defined a class and it is inheriting everything form the class Model
    fuel_types = {
        "D":"Diesel",
        "P":"Petrol"
    }
    name = models.CharField(max_length=100)
    yop = models.IntegerField()
    description = models.CharField(max_length=250)
    fuelType = models.CharField(max_length=1, choices = fuel_types)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name