from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateTaskForm , UpdateUserForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from  django.contrib import messages

def home(request):
    return render(request, 'index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The user was registered succesfully!")
            return redirect("my-login")
        
    context = {'form': form}
    return render(request, 'register.html', context=context)


def my_login(request):
    form = LoginForm
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get ('password' )
            user = authenticate (request, username=username, password=password)
            if user is not None:
             auth. login (request, user)
             return redirect ("dashboard")
    context = { "form" : form }
    return render(request, 'my-login.html',context=context)



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


@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'profile/dashboard.html')

@login_required(login_url='my-login')
def profile_management(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance = request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect("dashboard")
    user_form = UpdateUserForm(instance=request.user)
    context ={"user_form": user_form}
    return render(request, 'profile/profile-management.html',context=context)
        


def user_logout(request):
    auth.logout(request)
    return redirect("")

@login_required(login_url='my-login')
def createTask(request):
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("view-tasks")
            
    context = {'form':form}
    return render(request, 'profile/create-task.html', context=context)




@login_required(login_url='my-login')
def viewTask(request):
    current_user = request.user.id
    task = Task.objects.all().filter()
    context = {'task':task}
    return render(request, 'profile/view-task.html', context=context)


@login_required(login_url='my-login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTaskForm(instance=task)
    if request.method == 'POST':
        form =  CreateTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('view-tasks')
        
    context = {'form': form}    
    return render(request, 'profile/update-task.html', context=context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('view-tasks')
    return render(request, 'profile/delete-task.html')


@login_required(login_url='my-login')
def deleteAccount(request):
    if request.method == 'POST':
        deleteUser = User.objects.get(username=request.user)
        deleteUser.delete()
        return redirect("")
    
    return  render(request, "profile/delete-account.html")