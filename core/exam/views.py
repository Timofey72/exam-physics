from django.shortcuts import render
from django.http import Http404

from .models import Task, TaskCategory, Variant, FormulaCategory


def index(request):
    formula_categories = FormulaCategory.objects.all()[:3]
    context = {'formula_categories': formula_categories}
    return render(request, 'exam/index.html', context)


def variants(request):
    variants_list = Variant.objects.all().order_by('variant_number')

    context = {'variants': variants_list}
    return render(request, 'exam/variants.html', context)


def single_variant(request, variant_id):
    variant = Variant.objects.filter(variant_number=variant_id)
    if not variant.exists():
        raise Http404("Variant does not exist")

    context = {'variant': variant.first()}
    return render(request, 'exam/singleVariant.html', context)


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
    formulas_categories = FormulaCategory.objects.all()

    context = {'f_categories': formulas_categories}
    return render(request, 'exam/formulas.html', context)


def docs(request):
    return render(request, 'exam/docs.html')


def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)


def handler500(request, *args, **argv):
    return render(request, 'errors/500.html', status=500)
