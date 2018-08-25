import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=200)
    register_date = models.DateTimeField('date published')
    brand= models.CharField(max_length=100)
