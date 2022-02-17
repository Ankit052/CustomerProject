import profile
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=120,unique=True)
    mobile_no = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.first_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    profile_number = models.CharField(max_length=9)
    created_on = models.DateTimeField(auto_now_add= True)