from django.db import models

# Create your models here.

class User(models.Model):
    number=models.IntegerField()
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name