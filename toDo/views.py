
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from toDo.utils import create_new_task, update_task_status, update_task_all


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        result = create_new_task(data)
        if result.get('success', False):
            return JsonResponse({'message': result['message']})
        else:
            return JsonResponse({'error': result['error']},
                                status=400 if 'User does not exist' in result['error'] else 500)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


@csrf_exempt
def update_status(request, task_id):
    if request.method == 'PATCH':
        data = json.loads(request.body.decode('utf-8'))
        new_status = data.get('status')

        result = update_task_status(task_id, new_status)
        if result.get('success', False):
            return JsonResponse({'message': result['message']})
        else:
            return JsonResponse({'error': result['message']}, status=400)
    else:
        return JsonResponse({'error': 'Only PATCH method is allowed'}, status=405)

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'PATCH':
        data = json.loads(request.body.decode('utf-8'))
        result = update_task_all(task_id, data)
        if result.get('success', False):
            return JsonResponse({'message': result['message']})
        else:
            return JsonResponse({'error': result['message']}, status=400)
    else:
        return JsonResponse({'error': 'Only PATCH method is allowed'}, status=405)
