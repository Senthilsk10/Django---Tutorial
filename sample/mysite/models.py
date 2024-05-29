from django.db import models
from django.contrib.auth.models import User
class Movie(models.Model):
    name = models.CharField(max_length=45,blank=True, null=True)
    year = models.DateField()
    actor = models.CharField(max_length=20,blank=True, null=True)
    actoress = models.CharField(max_length=20,blank=True, null=True)
    

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')