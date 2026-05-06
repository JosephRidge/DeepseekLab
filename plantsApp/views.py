from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    context = {}
    return render(request, "base.html", context)

def about(request):
    return HttpResponse("Welcome to Deepseeks about page!! \n\nhttp://127.0.0.1:8000/about/")
 

def species(request):
    students = Student.objects.all()
    context = {"data":students }
    return render(request,"plantsApp/species.html", context) 


def locations(request):
    context = { }
    return render(request,"plantsApp/locations.html", context) 

def medicinal(request):
    context = { }
    return render(request,"plantsApp/medicinal.html", context) 

