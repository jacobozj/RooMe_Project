from django.db import models

# Create your models here.
class Rooms(models.Model):
    description=models.CharField(max_length=100)
    price=models.IntegerField()
    location=models.CharField(max_length=20)
    reserved=models.BooleanField(default=False)
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    area=models.IntegerField()
    
  