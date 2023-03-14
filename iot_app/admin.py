from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'timestamp')
    list_filter = ('name',)
    search_fields = ('name', 'value')
    ordering = ('-timestamp',)
    readonly_fields = ('name', 'value', 'timestamp')

    def has_add_permission(self, request):
        return False

admin.site.register(Data, DataAdmin)
