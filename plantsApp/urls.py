from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.home, name='plants-home'),
    path('species/', views.species, name ='plant-species'),
    path('locations/', views.locations, name ='plants-locations'),
    path('medicinal-plants/', views.medicinal, name ='medicinal-plants'),
]
