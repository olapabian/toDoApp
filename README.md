
Aby uruchomić serwer należy w pliku settings.py ustawić parametry domyślnej bazy danych PostgeSQL w tym miejscu:
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
