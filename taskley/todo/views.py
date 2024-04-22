from django.shortcuts import render,redirect
from .modals import Task
from .forms import TaskModalForm
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
            context = {'form': form}
    return render(request, 'register.html', context=context)

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


@Login_required(login_url='my-login')

def dashboard(request):
    return render(request, 'profile/dashboard.html')





@Login_required(login_url='my-login')

def createTask(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard') 
    context = {'form':form}
    return render(request, 'profile/create-task.html', context=context)

def updateTask(request):
    context = {'form':form}
    return render(request, 'profile/update-task.html', context=context)