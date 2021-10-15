from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    description = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.title

