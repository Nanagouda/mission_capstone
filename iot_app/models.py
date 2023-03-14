from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
            app_label = 'iot_app'

@staticmethod
def store_data(device_id, token, payload):
    # Verify device ID and token
    if device_id != 'test_device' or token != 'test_token':
        return {'error': 'Invalid device ID or token'}

    # Store data in database
    for name, value in payload.items():
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
    return {'status': 'Data stored successfully'}

@staticmethod
def get_latest_data():
    # Get the latest data from the database
    latest_data = {}
    latest_data['Temperature'] = Data.objects.filter(name='Temperature').last().value
    latest_data['Humidity'] = Data.objects.filter(name='Humidity').last().value
    latest_data['Voltage'] = Data.objects.filter(name='Voltage').last().value
    latest_data['Current'] = Data.objects.filter(name='Current').last().value
    latest_data['Object Temperature'] = Data.objects.filter(name='Object Temperature').last().value

    # Return the latest data
    return latest_data
