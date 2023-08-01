from django.db import models

# Create your models here.
class Signup(models.Model):
    
    suser=models.CharField(max_length=50)
    semail=models.CharField(max_length=50)
    spassword=models.CharField(max_length=50)


class Search(models.Model):
    lcity=models.CharField(max_length=50)
    lguests=models.IntegerField()
    larrival=models.DateField(max_length=50)
    ldeparture=models.DateField(max_length=50)

class Book(models.Model):
    
    
    
    
    
    
    
    
    
    
    
