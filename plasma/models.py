from django.db import models

# Create your models here.

class Volunteer(models.Model):
    name = models.CharField(max_length = 200, null = False)
    phone = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    description = models.CharField(max_length = 300, null = True)
    date_joined = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name


class RegisterDonor(models.Model):
    name = models.CharField(max_length=200, null=False)
    phone = models.BigIntegerField(null = True)
    email = models.EmailField(max_length=200, null = True)
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('prefer not to say', 'prefer not to say'),
    )
   
    location = models.CharField(max_length= 200, null = True)
    BLOODGRP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    
    recoverydate = models.DateField(auto_now=False, auto_now_add=False)  
    bloodgroup = models.CharField(max_length=200, null=True, choices=BLOODGRP)

    date_joined = models.DateTimeField(auto_now_add=True)
    #models.CharField(max_length=200, null=True, choices=GENDER)

    def __str__(self):
        return self.name
