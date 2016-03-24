from django.core.urlresolvers import reverse

from api.models import GPS
from api.tests.utils import KrakSatAPITestCase


class GPSTests(KrakSatAPITestCase):
    """Tests for /gps API endpoint"""

    list_url = reverse('gps-list')
    model = GPS
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'latitude': 13.01, 'longitude': -50.07,
        'altitude': 213.065, 'direction': 20.5,
        'speed_over_ground': 11.13,
        'active_satellites': 5, 'quality': 'gps', 'hdop': 1.01
        # 'satellites_in_view': 11, 'fix_type': '3d', 'pdop': 5.1, 'vdop': 3.07
    }

    def test_create(self):
        """Ensure we can create a new GPS object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /gps returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Latitude below -90', {'latitude': -90.01}),
            ('Latitude above 90', {'latitude': 90.01}),
            ('Invalid latitude', {'latitude': 'foobar'}),
            ('Longitude below -180', {'longitude': -180.01}),
            ('Longitude above 180', {'longitude': 180.01}),
            ('Invalid longitude', {'longitude': 'foobar'}),
            ('Direction below -0', {'direction': -0.01}),
            ('Direction above 360', {'direction': 360.01}),
            ('Invalid direction', {'direction': 'foobar'}),
            ('Invalid speed over ground', {'speed_over_ground': 'foobar'}),
            ('Active satellites below 0', {'active_satellites': -1}),
            ('Invalid active satellites', {'active_satellites': 'foobar'}),
            # ('Satellites in view below 0', {'satellites_in_view': -1}),
            # ('Invalid satellites in view', {'satellites_in_view': 'foobar'}),
            ('Invalid quality', {'quality': 'foobar'}),
            # ('Invalid fix type', {'fix_type': 'foobar'}),
            # ('Invalid pdop', {'pdop': 'foobar'}),
            ('Invalid hdop', {'hdop': 'foobar'}),
            # ('Invalid vdop', {'vdop': 'foobar'}),
        )
