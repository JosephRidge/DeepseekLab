from django.contrib import admin 

#  import the models 
from .models import Animal

#  register the models in the admin panel 
admin.site.register(Animal)
