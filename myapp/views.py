from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse('<h2>Hello world %s</h2>' % username)

def about(request):
    return HttpResponse('About')

def projects(requests):                     
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(requests, title):
    task = Task.objects.get(title=title)
    ##task= get_object_or_404(Task, id=id)
    return HttpResponse('tasks: %s' % task.title)