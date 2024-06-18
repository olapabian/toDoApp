# toDo/utils.py (nazwij plik odpowiednio do Twojej aplikacji)
from django.contrib.auth.models import User

from toDo.models import Task
from django.contrib.auth.models import User
from django.db import transaction

def create_new_task(data):
    nazwa = data.get('nazwa')
    opis = data.get('opis')
    status = data.get('status')
    przypisany_uzytkownik_id = data.get('przypisany_uzytkownik')

    try:
        # Sprawdzamy, czy użytkownik o podanym ID istnieje
        user = User.objects.get(pk=przypisany_uzytkownik_id)
    except User.DoesNotExist:
        return {'success': False, 'message': 'User with provided ID does not exist'}

    try:
        with transaction.atomic():
            new_task = Task.objects.create(
                nazwa=nazwa,
                opis=opis,
                status=status,
                przypisany_uzytkownik=user
            )
    except Exception as e:
        # Obsługa ogólnego wyjątku w przypadku błędu tworzenia zadania
        return {'success': False, 'message': f'Failed to create task: {str(e)}'}

    return {'success': True, 'message': 'Task created successfully'}
