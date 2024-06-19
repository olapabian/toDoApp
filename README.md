Aby uruchomić aplikację należy w pliku settings.py ustawić parametry domyślnej bazy danych PostgeSQL w tym miejscu:
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
