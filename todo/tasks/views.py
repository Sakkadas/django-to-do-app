from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task


class TaskLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):
    model = Task
    template_name = 'tasks/main.html'
    context_object_name = 'tasks'


class DetailTask(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    template_name = 'tasks/create_task.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks')
