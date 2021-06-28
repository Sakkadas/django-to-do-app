from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Task


class TaskList(ListView):
    model = Task
    template_name = 'tasks/main.html'
    context_object_name = 'tasks'

class CreateTask():
    pass