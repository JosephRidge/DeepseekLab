from django.db import models

# Create your models here.

"""
 - A model is a single representation of data to be storeed in our DB
 Steps:
 - Define a model
 - state the attributes and attach/ define its respective type
 
"""
class Animal(models.Model):
    name = models.CharField(max_length=100) # defined a string attribute for animal
    age = models.IntegerField()
    dob = models.DateTimeField()
    specie = models.CharField(max_length=200)
    bio = models.CharField(max_length=255)
    weight = models.FloatField()
    image =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}, {self.age} yrs old!"


