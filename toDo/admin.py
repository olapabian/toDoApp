from django.contrib import admin
from .models import Task, User, Old_Task
admin.site.register(Task)
admin.site.register(Old_Task)
admin.site.register(User)