from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Color(models.Model):
    name = models.CharField(max_length=100)
    hexa =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name