from django.core.urlresolvers import reverse

from api.models import SHT
from api.tests.utils import KrakSatAPITestCase


class SHTTests(KrakSatAPITestCase):
    """Tests for /sht API endpoint"""

    list_url = reverse('sht-list')
    model = SHT
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'humidity': 20, 'temperature': 30
    }

    def test_create(self):
        """Ensure we can create a new SHT object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /sht returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Humidity below 0', {'humidity': -5}),
            ('Humidity above 100', {'humidity': 100.04}),
            ('Temperature below -40', {'temperature': -40.01}),
            ('Temperature above 125', {'temperature': 125.01}),
        )
