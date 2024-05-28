from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=45,blank=True, null=True)
    year = models.DateField()
    actor = models.CharField(max_length=20,blank=True, null=True)
    actoress = models.CharField(max_length=20,blank=True, null=True)
    
