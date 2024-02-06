from django.contrib import admin

from devices.models import Devices, Location

# Register your models here.

admin.site.register(Location)
admin.site.register(Devices)
