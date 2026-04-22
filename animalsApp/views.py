from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {} # purpose if hold a refe to the data
    return render (request,"animalsApp/home.html", context)

def about(request):
    context={}
    return render(request,"animalsApp/about.html", context)