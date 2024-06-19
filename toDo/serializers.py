

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task, Old_Task


class CreateTaskSerializer(serializers.ModelSerializer):
    przypisany_uzytkownik = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False,
                                                               allow_null=True)
    class Meta:
        model = Task
        fields = ['nazwa', 'status', 'przypisany_uzytkownik', 'opis']
        extra_kwargs = {
            'nazwa': {'required': True},
            'status': {'required': False},
            'opis': {'required': False},
        }

class UpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']
        extra_kwargs = {
            'status': {'required': True},
        }


class OptionalTaskSerializer(serializers.ModelSerializer):
    przypisany_uzytkownik = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False,
                                                               allow_null=True)
    class Meta:
        model = Task
        fields = ['nazwa', 'status', 'przypisany_uzytkownik', 'opis']
        extra_kwargs = {
            'nazwa': {'required': False},
            'status': {'required': False},
            'opis': {'required': False}
        }

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'nazwa', 'opis', 'status', 'date', 'przypisany_uzytkownik']
class OldTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Old_Task
        fields = ['id', 'nazwa', 'opis', 'status', 'date', 'przypisany_uzytkownik','task_id']