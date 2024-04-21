from django.shortcuts import render

# Create your views here.
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_manager/templates/task_list.html', {'tasks': tasks})

# Add views for creating, updating, and deleting tasks
