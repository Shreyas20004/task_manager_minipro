from django.shortcuts import render,redirect
from .modals import Task
from .forms import TaskModalForm
from django.http import HttpResponse

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

def create_task(request):
    form = TaskModalForm()
    if request.method=="POST":
        form =TaskModalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved!!")
        context = { "form" : form }
    return render(request, 'task-form.html',context=context)


def view_task(request):
   tasks = Task.objects.all()
   context = { "tasks" : tasks }
   return render(request, 'task-form.html',context=context)