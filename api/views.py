import rest_framework
from rest_framework import viewsets

from api.models import SHT, IMU, GPS
from api.serializers import SHTSerializer, IMUSerializer, GPSSerializer


def get_view_name(view_cls, suffix=None):
    """Return the view name to be shown to a user.

    The function allows to specify display_name attribute for a view to be
    displayed as view name in OPTIONS responses and browsable API.
    """
    if hasattr(view_cls, 'display_name'):
        name = view_cls.display_name
        if suffix:
            name += ' ' + suffix
        return name
    if view_cls.__name__ == 'APIRoot':
        return 'API Root'

    return rest_framework.views.get_view_name(view_cls, suffix)


class SHTViewSet(viewsets.ModelViewSet):
    """SHT (Humidity and Temperature) sensor data."""
    display_name = 'SHT Data'
    queryset = SHT.objects.all()
    serializer_class = SHTSerializer


class IMUViewSet(viewsets.ModelViewSet):
    """IMU (Inertial Measurement Unit) sensor data."""
    display_name = 'IMU Data'
    queryset = IMU.objects.all()
    serializer_class = IMUSerializer


class GPSViewSet(viewsets.ModelViewSet):
    """GPS (Global Positioning System) fix data."""
    display_name = 'GPS Fix Data'
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
