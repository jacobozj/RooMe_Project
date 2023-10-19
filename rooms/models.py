from django.db import models
from datetime import datetime

# Create your models here.
class Rooms(models.Model):
    title=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    location=models.CharField(max_length=20)
    reserved=models.BooleanField(default=False)
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    area=models.IntegerField()
    garage=models.IntegerField(default=0)
    city=models.CharField(max_length=20,default="")
    state=models.CharField(max_length=20,default="")
    image=models.ImageField(upload_to='rooms/images/', default="")
    image2=models.ImageField(upload_to='rooms/images/', default="", blank=True)
    image3=models.ImageField(upload_to='rooms/images/', default="", blank=True)
    image4=models.ImageField(upload_to='rooms/images/', default="", blank=True)
    image5=models.ImageField(upload_to='rooms/images/', default="", blank=True)
    fecha=models.DateField(default=datetime.now, blank=True)
    renter=models.CharField(max_length=50, default="")
