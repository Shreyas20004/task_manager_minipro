from django.db import models

# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=85)
    
    content = models.CharField(max_length=300)
    
    date_posted = models.DateField( auto_now_add=True)
    
class Review(models.Model):
    Reviewer_name = models.CharField(max_length=85)
    Reviewer_title = models.CharField(max_length=100)
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE)