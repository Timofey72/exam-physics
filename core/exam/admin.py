from django.contrib import admin
from django.contrib.auth.models import Group

from .models import TaskCategory, Task

admin.site.register(TaskCategory)
admin.site.register(Task)

admin.site.unregister(Group)
