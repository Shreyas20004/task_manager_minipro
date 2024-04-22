from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=100, null=True)
    
    content = models.CharField(max_length=1000, null=True, blank=True)
    
    date_posted = models.DateField( auto_now_add=True, null=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    
    