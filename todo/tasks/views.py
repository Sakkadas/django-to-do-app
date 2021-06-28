from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task


class TaskList(ListView):
    model = Task
    template_name = 'tasks/main.html'
    context_object_name = 'tasks'

class DetailTask(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'


class CreateTask():
    pass