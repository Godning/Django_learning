from django.db import models

# Create your models here.
class CMD(models.Model):
    cmd = models.CharField(max_length=30)
    result = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.cmd