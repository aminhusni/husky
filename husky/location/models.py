#Amin Husni - 2018
from django.db import models

# Create your models here.
class Location(models.Model):
    
    location_id = models.TextField(max_length=100)
    location_name = models.TextField(max_length=100)

    def __str__(self):
        return self.location_name