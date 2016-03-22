import django_filters
from django.forms import widgets

from api.models import (
    Photo, Telemetry, GPS, GSInfo, Status, PlanetaryData, Kundt
)


class TimestampFilterSet(django_filters.FilterSet):
    """Filter set that provides start_timestamp and end_timestamp filters"""
    start_timestamp = django_filters.IsoDateTimeFilter(
        name='timestamp', lookup_type='gt',
        widget=widgets.DateTimeInput(
                attrs={'type': 'datetime-local', 'step': '0.001'}),
        label='Start timestamp (greater than)')
    end_timestamp = django_filters.IsoDateTimeFilter(
        name='timestamp', lookup_type='lte',
        widget=widgets.DateTimeInput(
                attrs={'type': 'datetime-local', 'step': '0.001'}),
        label='End timestamp (less than or equal)')


class TelemetryFilter(TimestampFilterSet):
    class Meta:
        model = Telemetry
        fields = ()


class KundtFilter(TimestampFilterSet):
    frequency = django_filters.RangeFilter(name='frequency')

    class Meta:
        model = Kundt
        fields = ()


class GPSFilter(TimestampFilterSet):
    class Meta:
        model = GPS
        fields = ()


class PhotoFilter(TimestampFilterSet):
    class Meta:
        model = Photo
        fields = ('is_panorama',)


class GSInfoFilter(TimestampFilterSet):
    class Meta:
        model = GSInfo
        fields = ()


class StatusFilter(TimestampFilterSet):
    class Meta:
        model = Status
        fields = ()


class PlanetaryDataFilter(TimestampFilterSet):
    class Meta:
        model = PlanetaryData
        fields = ()
