from django.urls import  path
from . import views 
urlpatterns = [
    path('',views.home,name=""),
    
    
    path('register/',views.register,name="register"),
    
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('profile-management', views.profile_management, name="profile-management"),
    
    
    path('delete-account', views.deleteAccount, name="delete-account"),


    path('create-task', views.createTask, name="create-task"),


    path('view-task', views.viewTask, name="view-tasks" ),
    path('user-login', views.my_login, name="my-login" ),
    path('user-logout', views.user_logout, name="user-logout" ),

    
    path('update-task/<str:pk>/', views.updateTask, name="update-tasks" ),

    path('delete-task/<str:pk>/', views.deleteTask, name="delete-tasks" ),







]
