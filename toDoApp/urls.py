# urls.py

from django.contrib import admin
from django.urls import path
from toDo.views import create_task, update_status, update_task  # Import the update_status function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/create/', create_task, name='create_task'),
    path('task/<int:task_id>/update_status/', update_status, name='update_status'),
    path('task/<int:task_id>/update_task/', update_task, name='update_task'),
]
