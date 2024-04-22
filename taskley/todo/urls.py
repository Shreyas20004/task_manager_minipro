from django.urls import  path
from . import views 
urlpatterns = [
    path('',views.home,name=""),
    
    
    path('register/',views.register,name="register"),
    
    
    path('dashboard', views.dashboard, name="dashboard"),


    path('create-task', views.createTask, name="create-task"),


    path('view-task', views.viewTask, name="view-tasks" ),

    
    path('update-task/<str:pk>/', views.updateTask, name="update-tasks" ),

    path('delete-task/<str:pk>/', views.deleteTask, name="delete-tasks" ),







]
