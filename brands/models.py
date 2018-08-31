
from django.db import models
from django.utils import timezone
# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.brand_name
    #return u'{0}'.format(self.brand_name)
    #return "deneme"
