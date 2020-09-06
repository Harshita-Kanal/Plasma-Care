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