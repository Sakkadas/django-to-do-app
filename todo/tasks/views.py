from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class TaskRegisterView(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TaskRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        else:
            return super(TaskRegisterView, self).get(*args, **kwargs)


class TaskLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/taks_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        clear_input = self.request.GET.get('clear-area')
        if search_input:
            context['tasks'] = context['tasks'].filter(title__contains=search_input)
        elif clear_input:
            search_input = ''
            context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/create_task.html'
    fields = ['title', 'description', 'complete', 'important']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    fields = ['title', 'description', 'complete', 'important']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks')
