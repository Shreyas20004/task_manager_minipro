from django.urls import  path
from . import views 
urlpatterns = [
    path('',views.home),
    path('login/', views.login),
    path('register/',views.register),
    
    
    #cruds
    path('task-form/',views.create_task),
    path('read-task/',views.view_task),
    
]
