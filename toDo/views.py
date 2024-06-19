
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Task, save_old_task_state, Old_Task
from .serializers import CreateTaskSerializer, UpdateStatusSerializer, OptionalTaskSerializer, TasksSerializer, \
    OldTasksSerializer


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = CreateTaskSerializer(data=data)

        if serializer.is_valid():
            # Save the validated data to create a new task
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

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
            # Save the old task state before updating
            save_old_task_state(task)

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

        serializer = OptionalTaskSerializer(task, data=data, partial=True)

        if serializer.is_valid():
            # Save the old task state before updating
            save_old_task_state(task)

            serializer.save()
            return JsonResponse({'message': 'Task updated successfully'})
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only PATCH method is allowed'}, status=405)

@csrf_exempt
def get_tasks(request):
    if request.method == 'GET':
        # Get query parameters from the request
        id = request.GET.get('id')
        nazwa = request.GET.get('nazwa')
        opis = request.GET.get('opis')
        status = request.GET.get('status')
        uzytkownik = request.GET.get('uzytkownik')

        # Prepare queryset based on query parameters
        queryset = Task.objects.all()

        if id:
            queryset = queryset.filter(id=id)
        if nazwa:
            queryset = queryset.filter(nazwa__icontains=nazwa)
        if opis:
            queryset = queryset.filter(opis__icontains=opis)
        if status:
            queryset = queryset.filter(status=status)
        if uzytkownik:
            queryset = queryset.filter(przypisany_uzytkownik_id=uzytkownik)

        # Serialize the queryset of tasks
        serializer = TasksSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)
@csrf_exempt
def get_old_tasks(request):
    if request.method == 'GET':
        # Get query parameters from the request
        id = request.GET.get('id')
        nazwa = request.GET.get('nazwa')
        opis = request.GET.get('opis')
        status = request.GET.get('status')
        uzytkownik = request.GET.get('uzytkownik')
        task= request.GET.get('task_id')

        # Prepare queryset based on query parameters
        queryset = Old_Task.objects.all()

        if id:
            queryset = queryset.filter(id=id)
        if nazwa:
            queryset = queryset.filter(nazwa__icontains=nazwa)
        if opis:
            queryset = queryset.filter(opis__icontains=opis)
        if status:
            queryset = queryset.filter(status=status)
        if uzytkownik:
            queryset = queryset.filter(przypisany_uzytkownik_id=uzytkownik)
        if task:
            queryset = queryset.filter(task_id=task)

        # Serialize the queryset of tasks
        serializer = OldTasksSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)
@csrf_exempt
def get_task_by_id(request, task_id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

        serializer = TasksSerializer(task)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)


@csrf_exempt
def delete_task_by_id(request, task_id):
    if request.method == 'DELETE':
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)

        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)
