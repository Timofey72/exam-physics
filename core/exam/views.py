from django.shortcuts import render


def index(request):
    return render(request, 'exam/index.html')


def options(request):
    return render(request, 'exam/options.html')


def single_option(request, option_id):
    context = {'option_id': option_id}
    return render(request, 'exam/singleOption.html', context)


def tasks(request):
    return render(request, 'exam/tasks.html')


def single_task(request, task_id):
    context = {'task_id': task_id}
    return render(request, 'exam/singleTask.html', context)


def formulas(request):
    return render(request, 'exam/formulas.html')


def docs(request):
    return render(request, 'exam/docs.html')
