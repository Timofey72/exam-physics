from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('options', views.options, name='options'),
    path('options/<int:option_id>', views.single_option, name='single-option'),
    path('tasks', views.tasks, name='tasks'),
    path('tasks/<int:task_id>', views.single_task, name='single-task'),
    path('formulas', views.formulas, name='formulas'),
    path('docs', views.docs, name='docs'),
]
