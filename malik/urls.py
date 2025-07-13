
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('/dashboard', views.task_list, name="task_list"),
    path('About/', views.About, name="About"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    #    path('login/', views.login, name="login"),
    #    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('task/new/', views.task_create, name="task_create"),
    path('task/delete/', views.task_delete, name="task_delete"),
]

