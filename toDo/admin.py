from django.contrib import admin

from .models import Task, Old_Task
admin.site.register(Task)
admin.site.register(Old_Task)
