from django.shortcuts import render, redirect
from .models import todoList
from django.contrib import messages
from .forms import ToDoListForm
import datetime
from datetime import date

# Create your views here.


def index(request):
    todo_list = todoList.objects.all()
    upcoming_list = todoList.objects.filter(is_completed=False).order_by('-com_date')
    current_date = date.today()
    blink = False
    for i in upcoming_list:
        date_diff = (i.com_date - current_date).days
        if date_diff == 1:
            blink = True
            break

    form = ToDoListForm()
    if request.method == 'POST' and 'task-submit' in request.POST:
        form = ToDoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    elif request.method == 'POST':
        completed = request.POST.get('completed')
        task_id = request.POST.get('task-id')

        task = todoList.objects.filter(pk=task_id).first()
        if task:
            if completed:
                task.is_completed = True
            else:
                task.is_completed = False
            task.save()
            return redirect('index')

    context = {
        'tdlist': todo_list,
        'form': form,
        'upcoming_list': upcoming_list,
        'blink': blink,
    }
    return render(request, 'index.html', context)


def remove_task(request, task_id):
    todoList.objects.filter(pk=task_id).delete()
    return redirect('index')


