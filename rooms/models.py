from django.db import models

# Create your models here.
class Rooms(models.Model):
    title=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=100)
    price=models.IntegerField()
    location=models.CharField(max_length=20)
    reserved=models.BooleanField(default=False)
    bedrooms=models.IntegerField()
    bathrooms=models.IntegerField()
    area=models.IntegerField()
    garage=models.IntegerField(default=0)
    city=models.CharField(max_length=20,default="")
    state=models.CharField(max_length=20,default="")
    image1=models.ImageField(upload_to='rooms/images/', default="")
    image2=models.ImageField(upload_to='rooms/images/', default="")
    image3=models.ImageField(upload_to='rooms/images/', default="")
    image4=models.ImageField(upload_to='rooms/images/', default="")
    image5=models.ImageField(upload_to='rooms/images/', default="")
