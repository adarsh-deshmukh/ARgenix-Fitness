from time import timezone
from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError ("Email must contain @")

gender_choice=[("1","Male"),("2","Female"),("3","others"),("4","Don't want to disclose")]
goal_choice=[("1","Weight loose"),("2","Weight gain"),("3","Fitness"),("4","Bodybuilding")]

class Membership(models.Model):
    first_name=models.CharField(null=True,max_length=20)
    last_name=models.CharField(null=True,max_length=20)
    email=models.EmailField(null=True,unique=True,validators=[validate_email])
    contact=models.IntegerField(null=True,unique=True)
    Address=models.TextField(null=True)
    gender=models.CharField(null=True,max_length=50,choices=gender_choice)
    weight=models.IntegerField(null=True,help_text="Weight should be in KG")
    height=models.IntegerField(null=True,help_text="Height should be in CM")
    goal=models.CharField(null=True,max_length=50,choices=goal_choice)
     

    def __str__(self):
        return self.first_name and self.last_name

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    Admin=models.BooleanField(default=False)
    Member=models.BooleanField(default=False)
    username=models.CharField(null=True,max_length=10,unique=True)
    first_name=models.CharField(null=True,max_length=20)
    last_name=models.CharField(null=True,max_length=20)
    email=models.EmailField(null=True,unique=True,validators=[validate_email]) 
       

    def __str__(self):
        return self.username



