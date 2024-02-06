from ninja import NinjaAPI
from .models import Device, Location
from django.shortcuts import get_object_or_404
from devices.schemas import DeviceSchema, LocationSchema


app = NinjaAPI()


@app.get("devices/", response=list[DeviceSchema])
def get_devices(request):
    return Device.objects.all()

@app.get("devices/{slug}/", response=DeviceSchema)
def get_device(request, slug: str):
    device = get_object_or_404(Device, slug=slug)
    return device

@app.get("location/", response=list[LocationSchema])
def get_location(request):
    return Location.objects.all()
