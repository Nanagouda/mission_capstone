from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from .models import Data
import json


class RealtimeDataView(View):
    def get(self, request, *args, **kwargs):
        data = Data.objects.order_by('-timestamp')[:10] # Retrieve the last 10 entries
        data = [{'name': d.name, 'value': d.value, 'timestamp': d.timestamp} for d in data]
        return JsonResponse({'data': data})

    def post(self, request, *args, **kwargs):
        # Parse JSON payload from request body
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

        # Store data in database
        for name, value in payload.items():
            if name in ['Temperature', 'Humidity', 'Voltage', 'Current', 'Object Temperature']:
                Data.objects.create(name=name, value=value)

        # Return success response
        return JsonResponse({'status': 'Data stored successfully'})


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Data
import json


@csrf_exempt
def store_data(request, device_id, token):
    # Verify device ID and token
    if device_id != 'test_device' or token != 'test_token':
        return JsonResponse({'error': 'Invalid device ID or token'}, status=401)

    # Parse JSON payload from request body
    try:
        payload = json.loads(request.body)
        print("Received JSON Payload: ", payload)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON payload'}, status=400)

    # Store data in database
    for name, value in payload.items():
        if name in ['temperature', 'humidity', 'voltage', 'current', 'object_temperature']:
            if name == 'temperature':
                Data.objects.create(name='Temperature', value=value)
            elif name == 'humidity':
                Data.objects.create(name='Humidity', value=value)
            elif name == 'voltage':
                Data.objects.create(name='Voltage', value=value)
            elif name == 'current':
                Data.objects.create(name='Current', value=value)
            elif name == 'object_temperature':
                Data.objects.create(name='Object Temperature', value=value)

    # Return success response
    return JsonResponse({'status': 'Data stored successfully'})


from django.shortcuts import render
from .models import Data

def latest_data_view(request):
    latest_data = []
    latest_data.append(('Temperature', Data.objects.filter(name='Temperature').last().value, Data.objects.filter(name='Temperature').last().timestamp))
    latest_data.append(('Humidity', Data.objects.filter(name='Humidity').last().value, Data.objects.filter(name='Humidity').last().timestamp))
    latest_data.append(('Voltage', Data.objects.filter(name='Voltage').last().value, Data.objects.filter(name='Voltage').last().timestamp))
    latest_data.append(('Current', Data.objects.filter(name='Current').last().value, Data.objects.filter(name='Current').last().timestamp))
    latest_data.append(('Object Temperature', Data.objects.filter(name='Object Temperature').last().value, Data.objects.filter(name='Object Temperature').last().timestamp))
    context = {'latest_data': latest_data}
    return render(request, 'latest_data.html', {'latest_data': latest_data})


