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
    Q1 = models.IntegerField()
    Q2 = models.IntegerField()
    Q3 = models.IntegerField()
    Q4 = models.IntegerField()
    Q5 = models.IntegerField()
    Q6 = models.IntegerField()
    Q7 = models.IntegerField()
    Q8 = models.IntegerField()
    Q9 = models.IntegerField()
    Q10 = models.CharField(max_length=100)

