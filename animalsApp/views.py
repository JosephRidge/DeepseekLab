from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

# Create your views here.

def home(request):
    animals  = Animal.objects.all() # fetch all the animals data from the DB
    context = {"data": animals} # purpose if hold a refe to the data
    return render (request,"animalsApp/home.html", context)

def about(request): 
    animals  = Animal.objects.get(id="1") # fetch all the animals data from the DB
    context = {"data": animals} # purpose if hold a refe to the data
    return render(request,"animalsApp/about.html", context)

def contact(request):
    context = {}
    return render(request, "animalsApp/contacts.html", context)