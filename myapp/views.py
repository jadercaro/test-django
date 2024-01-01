from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, get_list_or_404

# Create your views here.
def index(request):
    return render(request,"index.html")

def hello(request, username):
    return HttpResponse('<h2>Hello world... %s</h2>' % username)

def about(request):
    return render(request,'about.html')

def projects(requests):                     
    projects = list(Project.objects.values())
    return render(requests, 'projects.html')

def tasks(requests):
    #task = Task.objects.get(title=title)
    ##task= get_object_or_404(Task, id=id)
    return render(requests, 'tasks.html')