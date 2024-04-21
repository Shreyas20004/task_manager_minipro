from django.shortcuts import render


def register(request):
    return render(request, 'register.html')

def login(request):
     return render(request, 'login.html')

def dashboard(request):
     return render(request, 'dashboard.html')
 
def base(request):
    return render(request ,'base.html')

def home(request):
    return render(request, 'index.html')




