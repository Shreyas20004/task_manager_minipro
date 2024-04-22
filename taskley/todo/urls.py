from django.urls import  path
from . import views 
urlpatterns = [
    path('',views.home,name=""),
    
    
    path('register/',views.register,name="register"),
    
    
    path('dashboard', views.dashboard, name="dashboard"),


    path('my-login', views.my_login, name="my-login"),
    
    path("user-logout", views.my_logout, name='user-logout'),


    path('create-task', views.create_task, name="create-task"),


    path('view-tasks', views.view_task, name="view-tasks" ),






]
