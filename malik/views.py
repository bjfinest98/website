from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from django.contrib.auth.decorators import login_required
from .form import TaskForm

# Create your views here.


def Home (request):
    return render(request, "index.html")

def About (request):
    return render(request, "About.html")

def contact (request):
    return render(request, "contact.html")

def services (request):
    return render(request, "services.html")

# def login (request):
#     return render(request,"regristration/login.html")

# def logout (request):
#     return render(request,"regristration/logout.html")

def signup (request):
    if request.method == 'POST':
        form =UserCreationForm
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('task_list')
    else:
         form =UserCreationForm
    return render(request,"registration/signup.html",{'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request,'task_list.html',{'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request,'task_create.html',{'form': form})



@login_required
def task_delete(request,task_id):
    task = get_object_or_404(Task,id=task_id,user=request.user)
    task.delete
    return redirect('task_list')