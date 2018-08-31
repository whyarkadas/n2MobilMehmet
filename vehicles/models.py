from brands import models as brands
from django.db import models
from django.utils import timezone

# Create your models here.

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=200)
    register_date = models.CharField(max_length=80)
    brand= models.ForeignKey(brands.Brand, on_delete=models.CASCADE)