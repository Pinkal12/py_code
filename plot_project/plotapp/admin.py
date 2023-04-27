from django.contrib import admin
from .models import Anomaly

@admin.register(Anomaly)
# seclet cim you want
class AnomalyAdmin(admin.ModelAdmin):
    list_display = ('anomaly_number', 'anomaly_type', 'lat', 'lng', 'length', 'width', 'area', 'size', 'distance', 'location')
