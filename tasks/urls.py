from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle-task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete-task'),
]

