from django.urls import path
from . import views




urlpatterns = [
    path('',views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('hello/<str:username>',views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('createTask/', views.create_task, name='createTask'),
    path('createProject/', views.create_project, name='createProject'),

]