from django.contrib import admin
from django.urls import path
from iot_app.views import RealtimeDataView, store_data, latest_data_view



urlpatterns = [
    path("admin/", admin.site.urls),
    path('realtime-data/', RealtimeDataView.as_view(), name='realtime_data'),
    path('store-data/<str:device_id>/<str:token>', store_data, name='store_data'),
     path('latest-data/', latest_data_view, name='latest_data'),
]



