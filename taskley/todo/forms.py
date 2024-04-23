from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms
from . models import Task

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Title', 'content']
        exclude = ['user']
    
    
    
class UpdateUserForm(forms.ModelForm):
    password = None 
    class Meta:
        model = User
        fields = ['username', 'email',]
        exclude = ['password1','password2',]