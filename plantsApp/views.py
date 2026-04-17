from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Deepseek LAB!! \n\nhttp://127.0.0.1:8000/")


def about(request):
    return HttpResponse("Welcome to Deepseeks about page!! \n\nhttp://127.0.0.1:8000/about/")
