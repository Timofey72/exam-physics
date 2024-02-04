from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('variants/', views.variants, name='variants'),
    path('variants/<int:variant_id>/', views.single_variant, name='single-variant'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.single_task, name='single-task'),
    path('formulas/', views.formulas, name='formulas'),
    path('docs/', views.docs, name='docs'),
]
