from pyexpat import model
from django.db import models

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=100)
    stock_code = models.CharField(max_length=100)
    
    
class Users(models.Model):
    stock_code = models.ForeignKey(Companies, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    gender = models.CharField(max_length=50) 
    salary_band = models.CharField(max_length=100)
    Q1 = models.IntegerField(default=-1)
    Q2 = models.IntegerField(default=-1)
    Q3 = models.IntegerField(default=-1)
    Q4 = models.IntegerField(default=-1)
    Q5 = models.IntegerField(default=-1)
    Q6 = models.IntegerField(default=-1)
    Q7 = models.IntegerField(default=-1)
    Q8 = models.IntegerField(default=-1)
    Q9 = models.IntegerField(default=-1)
    Q10 = models.IntegerField(default=-1)

