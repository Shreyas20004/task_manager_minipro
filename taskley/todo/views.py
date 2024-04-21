from django.shortcuts import render
from .modals import Task
from .forms import TaskModalForm

def register(request):
    return render(request, 'register.html')

def login(request):
     return render(request, 'login.html')

def dashboard(request):
     return render(request, 'dashboard.html')
 
def base(request):
    return render(request ,'base.html')

def home(request):
    
    query_all_data = Task.objects.all()
    
    context = {'tasks':query_all_data}
    
    return render(request, 'index.html',context=context)

def create_task_form(request):
    form = TaskModalForm()
    context =  {"form":form}
    return render(request, 'task-form.html',context=context)



