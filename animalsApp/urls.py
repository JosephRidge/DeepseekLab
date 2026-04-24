from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.home, name="animal-home"),
    path("about/", views.about, name ="animal-about"),
    path("contact-us/", views.contact, name ="animal-contact-us")
]