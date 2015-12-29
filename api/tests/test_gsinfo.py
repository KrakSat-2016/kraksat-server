from django.core.urlresolvers import reverse

from api.models import GSInfo
from api.tests.utils import KrakSatAPITestCase


class GSInfoTests(KrakSatAPITestCase):
    """Tests for /gsinfo API endpoint"""

    list_url = reverse('gsinfo-list')
    model = GSInfo
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'latitude': 3.004, 'longitude': -9.87, 'timezone': -60,
    }

    def test_create(self):
        """Ensure we can create a new GSInfo object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /gsinfo returns error 400"""
        self._test_invalid_params(
                ('Invalid timestamp', {'timestamp': 'foobar'}),
                ('Latitude below -90', {'latitude': -90.01}),
                ('Latitude above 90', {'latitude': 90.01}),
                ('Invalid latitude', {'latitude': 'foobar'}),
                ('Longitude below -180', {'longitude': -180.01}),
                ('Longitude above 180', {'longitude': 180.01}),
                ('Invalid longitude', {'longitude': 'foobar'}),
                ('Timezone below -24 * 60', {'timezone': -24 * 60 - 1}),
                ('Timezone above 24 * 60', {'timezone': 24 * 60 + 1}),
                ('Invalid timezone', {'timezone': 'foobar'}),
        )
