# urls.py

from django.contrib import admin
from django.urls import path
from toDo.views import create_task, update_status, update_task, get_tasks, \
    get_task_by_id, delete_task_by_id, get_old_tasks  # Import the update_status function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/create/', create_task, name='create_task'),
    path('task/<int:task_id>/update_status/', update_status, name='update_status'),
    path('task/<int:task_id>/update_task/', update_task, name='update_task'),
    path('task/get_tasks/', get_tasks, name='get_tasks'),
    path('task/get_task_by_id/<int:task_id>', get_task_by_id, name='get_task_by_id'),
    path('task/delete_task_by_id/<int:task_id>', delete_task_by_id, name='delete_task_by_id'),
    path('task/get_old_tasks/', get_old_tasks, name='get_old_tasks'),

]
