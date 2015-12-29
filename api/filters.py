import django_filters
from django.forms import widgets

from api.models import Photo, SHT, IMU, GPS, GSInfo


class TimestampFilterSet(django_filters.FilterSet):
    """Filter set that provides start_timestamp and end_timestamp filters"""
    start_timestamp = django_filters.IsoDateTimeFilter(
        name='timestamp', lookup_type='gt',
        widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Start timestamp (greater than)')
    end_timestamp = django_filters.IsoDateTimeFilter(
        name='timestamp', lookup_type='lte',
        widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='End timestamp (less than or equal)')


class SHTFilter(TimestampFilterSet):
    class Meta:
        model = SHT
        fields = ()


class IMUFilter(TimestampFilterSet):
    class Meta:
        model = IMU
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
