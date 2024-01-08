from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from .forms import createNewTask

# Create your views here.
def index(request):
    title = 'Django course!!'
    return render(request,"index.html", {
        'title':title
    })

def hello(request, username):
    return HttpResponse('<h2>Hello world... %s</h2>' % username)

def about(request):
    return render(request,'about.html')

def projects(requests):                     
    #projects = list(Project.objects.valu es())
    projects = Project.objects.all()
    return render(requests, 'projects.html', {'projects':projects})

def tasks(requests):
    #task = Task.objects.get(title=title)
    ##task= get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(requests, 'tasks.html', {'tasks':tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': createNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'], project_id=2)
        return redirect('/tasks/')
        