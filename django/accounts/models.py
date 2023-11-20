from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    financial_products = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField()
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    
    
    # def __str__(self):
    #     return self.username