from django.db import models

# Create your models here.
class Users(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    username=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    confirm_password=models.CharField(max_length=45)
    program=models.CharField(max_length=45)
    sex=models.CharField(max_length=45)
    profile=models.CharField(max_length=15)

class Reseña(models.Model):
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    reseña=models.TextField()