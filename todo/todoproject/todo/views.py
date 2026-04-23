from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . models import Task


# Create your views here.


def task_list(request):
    task = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html',{'task':task})

def task_create(request):
    if request.method =='POST':
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()
        if title:
            Task.objects.create(title = title,description = description)
            return redirect(reverse('todo:task_list'))
        error = "title cannot be empty"
        return render(request, 'todo/task_form.html',{'error':error})
    return render(request,'todo/task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        
        if title:
        
            task.title = title
            task.description = description
            task.save()
            return redirect('todo:task_list') 
            
        error = "title cannot be empty"
        return render(request, 'todo/task_form.html', {'error': error, 'task': task})
    return render(request, 'todo/task_form.html', {'task': task})


def task_delete(request, pk):
    task =get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        task.delete()
        return redirect(reverse('todo:task_list'))
    return render(request,'todo/task_confirm_delete.html',{'task':task})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed # Toggle logic
    task.save()
    return redirect('todo:task_list')
            