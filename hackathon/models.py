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
    Q1 = models.CharField(max_length=100)
    Q2 = models.CharField(max_length=100)
    Q3 = models.CharField(max_length=100)
    Q4 = models.CharField(max_length=100)
    Q5 = models.CharField(max_length=100)
    Q6 = models.CharField(max_length=100)
    Q7 = models.CharField(max_length=100)
    Q8 = models.CharField(max_length=100)
    Q9 = models.CharField(max_length=100)
    Q10 = models.IntegerField(default=-1)

