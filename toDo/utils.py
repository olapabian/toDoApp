from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import get_object_or_404

from toDo.models import Task


def create_new_task(data):
    nazwa = data.get('nazwa')
    opis = data.get('opis')
    przypisany_uzytkownik_id = data.get('przypisany_uzytkownik')

    try:
        if przypisany_uzytkownik_id:
            user = User.objects.get(pk=przypisany_uzytkownik_id)
        else:
            user = None
    except User.DoesNotExist:
        return {'success': False, 'message': 'User with provided ID does not exist'}

    try:
        with transaction.atomic():
            new_task = Task.objects.create(
                nazwa=nazwa,
                opis=opis,
                przypisany_uzytkownik=user
            )
    except Exception as e:
        return {'success': False, 'message': f'Failed to create task: {str(e)}'}

    return {'success': True, 'message': 'Task created successfully'}


def update_task_status(task_id, new_status):
    if new_status is None:
        return {'success': False, 'message': 'Status not provided'}

    task = get_object_or_404(Task, pk=task_id)
    task.status = new_status
    task.save()

    return {'success': True, 'message': 'Task status updated successfully'}


def update_task_all(task_id, data):
    nazwa = data.get('nazwa')
    opis = data.get('opis')
    przypisany_uzytkownik_id = data.get('przypisany_uzytkownik')
    new_status = data.get('status')

    task = get_object_or_404(Task, pk=task_id)
    user = User.objects.get(pk=przypisany_uzytkownik_id)

    task.status = new_status
    task.nazwa = nazwa
    task.opis = opis
    task.przypisany_uzytkownik=user
    task.save()
    return {'success': True, 'message': 'Task status updated successfully'}
