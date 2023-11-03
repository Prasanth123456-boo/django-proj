from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=250)
    age= models.IntegerField(null=True)

    

class movie1(models.Model):
    name = models.CharField(max_length=250)
    age= models.CharField(max_length=100)
