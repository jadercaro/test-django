from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from .forms import createNewTask, createNewProject

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
    return render(requests, 'projects/projects.html', {'projects':projects})

def tasks(requests):
    #task = Task.objects.get(title=title)
    ##task= get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(requests, 'tasks/tasks.html', {'tasks':tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': createNewTask()})
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form':createNewProject()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project=id)
    print(project)
    return render(request, 'projects/details.html',{
        'project':project,
        'tasks':tasks})
        