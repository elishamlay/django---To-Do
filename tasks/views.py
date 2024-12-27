from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed  # Toggle completion status
    task.save()
    return redirect('task-list')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()  # Delete the task
    return redirect('task-list')
