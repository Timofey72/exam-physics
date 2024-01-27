from django.shortcuts import render
from django.http import Http404

from .models import Task, TaskCategory


def index(request):
    return render(request, 'exam/index.html')


def options(request):
    return render(request, 'exam/options.html')


def single_option(request, option_id):
    context = {'option_id': option_id}
    return render(request, 'exam/singleOption.html', context)


def tasks(request):
    categories = TaskCategory.objects.all()

    context = {'categories': categories}
    return render(request, 'exam/tasks.html', context)


def single_task(request, task_id):
    task = Task.objects.filter(id=task_id)
    if not task.exists():
        raise Http404("Task does not exist")

    context = {'task': task.first()}
    return render(request, 'exam/singleTask.html', context)


def formulas(request):
    return render(request, 'exam/formulas.html')


def docs(request):
    return render(request, 'exam/docs.html')


def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)
