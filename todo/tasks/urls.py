from django.urls import path
from .views import TaskList, DetailTask, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', DetailTask.as_view(), name='task'),

    path('create-task', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
]
