from django.contrib import admin
from traffic.models import Record, VehicleCount

# Register your models here.
admin.site.register(Record)
admin.site.register(VehicleCount)