from unicodedata import name
from django.db import models

# Create your models here.
class createmovies(models.Model):
    name = models.CharField(max_length=125)
    disc = models.CharField(max_length=450)
    filepic = models.URLField()
    link = models.URLField()
    
    def __str__(self):
        return self.name
class createanime(models.Model):
    name = models.CharField(max_length=125)
    disc = models.CharField(max_length=450)
    filepic = models.URLField()
    link = models.URLField()
    
    def __str__(self):
        return self.name