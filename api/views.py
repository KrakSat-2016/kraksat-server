import rest_framework
from rest_framework import viewsets

from api.filters import (
    PhotoFilter, TelemetryFilter, GPSFilter, GSInfoFilter, StatusFilter,
    PlanetaryDataFilter, KundtFilter, VideoInfoFilter
)
from api.mixins import TimestampOrderingMixin, LatestRecordModelViewSet
from api.models import (
    Telemetry, GPS, Photo, GSInfo, Status, PlanetaryData, Kundt, VideoInfo
)
from api.serializers import (
    TelemetrySerializer, GPSSerializer, PhotoSerializer, GSInfoSerializer,
    StatusSerializer, PlanetaryDataSerializer, KundtSerializer,
    VideoInfoSerializer
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


class TelemetryViewSet(LatestRecordModelViewSet, TimestampOrderingMixin):
    """Telemetry data."""
    display_name = 'Telemetry Data'
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer
    filter_class = TelemetryFilter


class KundtViewSet(LatestRecordModelViewSet, TimestampOrderingMixin):
    """Kundt's tube data."""
    display_name = "Kundt's Tube Data"
    queryset = Kundt.objects.all()
    serializer_class = KundtSerializer
    filter_class = KundtFilter


class GPSViewSet(LatestRecordModelViewSet, TimestampOrderingMixin):
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


class GSInfoViewSet(LatestRecordModelViewSet, TimestampOrderingMixin):
    """Information about the Ground Station."""
    queryset = GSInfo.objects.all()
    serializer_class = GSInfoSerializer
    filter_class = GSInfoFilter
    display_name = 'Ground Station Info'


class StatusViewSet(LatestRecordModelViewSet, TimestampOrderingMixin):
    """Mission status."""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_class = StatusFilter
    display_name = 'Mission Status'


class PlanetaryDataViewSet(LatestRecordModelViewSet, TimestampOrderingMixin):
    """Calculated planetary data."""
    queryset = PlanetaryData.objects.all()
    serializer_class = PlanetaryDataSerializer
    filter_class = PlanetaryDataFilter


class VideoInfoViewSet(LatestRecordModelViewSet, TimestampOrderingMixin):
    """
    Live Stream/Video Info for displaying the video from the probe's camera.
    """
    queryset = VideoInfo.objects.all()
    serializer_class = VideoInfoSerializer
    filter_class = VideoInfoFilter
