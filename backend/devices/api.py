from ninja import NinjaAPI
from .models import Device, Location
from django.shortcuts import get_object_or_404
from devices.schemas import (
    DeviceSchema,
    LocationSchema,
    DeviceCreateSchema,
    Error,
    DeviceLocationPath,
)


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


@app.post("device/", response={200: DeviceSchema, 404: Error})
def create_device(request, device: DeviceCreateSchema):
    if device.location_id:
        # we have a location ID in the body
        location_exists = Location.objects.filter(id=device.location_id).exists()
        if not location_exists:
            return 404, {"message": "location not found"}

    device_data = device.model_dump()
    device_model = Device.objects.create(**device_data)
    return device_model


@app.post("device/{device_slug}/set-location", response=DeviceSchema)
def update_device_location(request, device_slug, location: DeviceLocationPath):
    device = get_object_or_404(Device, slug=device_slug)
    if location.location_id:
        location = get_object_or_404(Location, id=location.location_id)
        device.location = location
    else:
        device.location = None
    device.save()
    return device

