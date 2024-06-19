# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from toDo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    przypisany_uzytkownik = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False, allow_null=True)
    class Meta:
        model = Task
        fields = ['nazwa', 'opis','status' 'przypisany_uzytkownik']
