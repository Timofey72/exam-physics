from django.contrib import admin
from django.contrib.auth.models import Group

from .models import TaskCategory, Task, Variant, FormulaCategory, Formula

admin.site.register(TaskCategory)
admin.site.register(Task)
admin.site.register(Variant)

admin.site.register(FormulaCategory)
admin.site.register(Formula)

admin.site.unregister(Group)
