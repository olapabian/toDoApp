
Aby uruchomić serwer należy w pliku settings.py ustawić parametry bazy danych PostgeSQL w tym miejscu (ja użyłam PostgreSQL 16):
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

Następnie przeprowadzić migracje bazy danych poleceniem: python manage.py migrate 
Polecenie stworzy tabele i uzupełni tabele auth_user przykładowymi danymi.

Kolejnym krokiem jest uruchomienie serwera komendą 
python manage.py runserver

W pliku toDoAppDjango.postman_collection.json znajduje się kolekcja endpointów wykorzystywanych przez serwer z przykładami użycia (przykłady ścieżek url, parametrów i ciał zapytań)
Kolekcje można zaimportować w Postmanie.

