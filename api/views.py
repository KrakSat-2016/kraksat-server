import rest_framework
from rest_framework import viewsets

from api.filters import (
    PhotoFilter, IMUFilter, SHTFilter, GPSFilter, GSInfoFilter, StatusFilter
)
from api.mixins import TimestampOrderingMixin, LatestRecordMixin
from api.models import SHT, IMU, GPS, Photo, GSInfo, Status
from api.serializers import (
    SHTSerializer, IMUSerializer, GPSSerializer, PhotoSerializer,
    GSInfoSerializer, StatusSerializer
)


def get_view_name(view_cls, suffix=None):
    """Return the view name to be shown to a user.

    The function allows to specify display_name attribute for a view to be
    displayed as view name in OPTIONS responses and browsable API.
    """
    if hasattr(view_cls, 'display_name'):
        name = view_cls.display_name
        if suffix and (not hasattr(view_cls, 'append_suffix') or
                       view_cls.append_suffix):
            name += ' ' + suffix
        return name
    if view_cls.__name__ == 'APIRoot':
        return 'API Root'

    return rest_framework.views.get_view_name(view_cls, suffix)


class SHTViewSet(viewsets.ModelViewSet, TimestampOrderingMixin):
    """SHT (Humidity and Temperature) sensor data."""
    display_name = 'SHT Data'
    queryset = SHT.objects.all()
    serializer_class = SHTSerializer
    filter_class = SHTFilter


class IMUViewSet(viewsets.ModelViewSet, TimestampOrderingMixin):
    """IMU (Inertial Measurement Unit) sensor data."""
    display_name = 'IMU Data'
    queryset = IMU.objects.all()
    serializer_class = IMUSerializer
    filter_class = IMUFilter


class GPSViewSet(viewsets.ModelViewSet, TimestampOrderingMixin):
    """GPS (Global Positioning System) fix data."""
    display_name = 'GPS Fix Data'
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
    filter_class = GPSFilter


class PhotoViewSet(viewsets.ModelViewSet, TimestampOrderingMixin):
    """Photos taken during the flight."""
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_class = PhotoFilter


class BaseGSInfoViewSet(viewsets.GenericViewSet):
    queryset = GSInfo.objects.all()
    serializer_class = GSInfoSerializer
    filter_class = GSInfoFilter


class GSInfoViewSet(BaseGSInfoViewSet, viewsets.ModelViewSet,
                    TimestampOrderingMixin):
    """Information about the Ground Station."""
    display_name = 'Ground Station Info'


class LatestGSInfoViewSet(BaseGSInfoViewSet, LatestRecordMixin):
    """Latest information about the Ground Station."""
    display_name = 'Latest Ground Station Info'


class BaseStatusViewSet(viewsets.GenericViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_class = StatusFilter


class StatusViewSet(BaseStatusViewSet, viewsets.ModelViewSet,
                    TimestampOrderingMixin):
    """Mission status."""
    display_name = 'Mission Status'


class LatestStatusViewSet(BaseStatusViewSet, LatestRecordMixin):
    """Latest mission status."""
    display_name = 'Latest Mission Status'
