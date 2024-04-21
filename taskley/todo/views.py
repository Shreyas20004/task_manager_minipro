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
    clientList = [
        {
            'id':1,
            'name':'John Doe',
            'job':"Web Developer",
            
            
        },
        
        {
            'id':2,
            'name':'Luke warren',
            'job':"Architect",
            
            
        }
    ]
    
    context={'client_list':clientList}
    return render(request, 'index.html',context=context)




