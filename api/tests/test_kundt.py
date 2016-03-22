from django.core.urlresolvers import reverse

from api.models import Kundt
from api.tests.utils import KrakSatAPITestCase


class KundtTests(KrakSatAPITestCase):
    """Tests for /kundt API endpoint"""

    list_url = reverse('kundt-list')
    model = Kundt
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'frequency': 2037.456, 'amplitude': 1000
    }

    def test_create(self):
        """Ensure we can create a new Telemetry object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /telemetry returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Frequency below 0', {'frequency': -0.001}),
            ('Amplitude below 0', {'amplitude': -1})
        )
