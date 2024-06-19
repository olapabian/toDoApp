from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('Nowy', 'Nowy'),
        ('W toku', 'W toku'),
        ('Rozwiązany', 'Rozwiązany'),
    ]

    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=255)
    opis = models.CharField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Nowy')
    date = models.DateTimeField(auto_now_add=True)
    przypisany_uzytkownik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nazwa



class Old_Task(models.Model):
    STATUS_CHOICES = [
        ('Nowy', 'Nowy'),
        ('W toku', 'W toku'),
        ('Rozwiązany', 'Rozwiązany'),
    ]
    task = models.ForeignKey(Task, on_delete=models.CASCADE)  # Many-to-one relation to Task
    id = models.AutoField
    nazwa = models.CharField(max_length=255)
    opis = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Nowy')
    date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now=True)
    przypisany_uzytkownik = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nazwa
