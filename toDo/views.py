# views.py

import json
from django.http import JsonResponse

from toDo.utils import create_new_task


def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        result = create_new_task(data)
        if result.get('success', False):
            return JsonResponse({'message': result['message']})
        else:
            return JsonResponse({'error': result['error']}, status=400 if 'User does not exist' in result['error'] else 500)

    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
