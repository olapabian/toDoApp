
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Task
from .serializers import CreateTaskSerializer, UpdateStatusSerializer, UpdateTaskSerializer


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        # Parse incoming JSON data using Django REST Framework's JSONParser
        data = JSONParser().parse(request)

        # Create an instance of the serializer with the parsed data
        serializer = CreateTaskSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data to create a new task
            serializer.save()
            return JsonResponse(serializer.data, status=201)  # Return serialized data with 201 Created status
        else:
            return JsonResponse(serializer.errors, status=400)  # Return validation errors with 400 Bad Request status

    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

@csrf_exempt
def update_status(request, task_id):
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

        serializer = UpdateStatusSerializer(task, data=data, partial=True)

        if 'status' not in data:
            return JsonResponse({'error': 'Status field is required'}, status=400)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'PATCH':
        data = json.loads(request.body.decode('utf-8'))
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

        serializer = UpdateTaskSerializer(task, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Task updated successfully'})
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only PATCH method is allowed'}, status=405)