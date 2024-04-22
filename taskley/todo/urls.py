from django.urls import  path
from . import views 
urlpatterns = [
    path('',views.home),
    path('login/', views.login),
    path('register/',views.register),
    
    
    #cruds
    path('task-form/',views.create_task),
    path('read-task/',views.view_task),
    path('update-task',views.update_task),
    
    # Applications

    path('my-login', views.my_login, name="my-login"),


    path('dashboard', views.dashboard, name="dashboard"),


    path('create-task', views.createTask, name="create-task"),


    path('view-tasks', views.viewTask, name="view-tasks" ),

    
    path('update-task/<str:pk>/', views.updateTask, name="update-tasks" ),







]
