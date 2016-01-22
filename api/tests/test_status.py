from django.core.urlresolvers import reverse

from api.models import Status
from api.tests.utils import KrakSatAPITestCase


class StatusTests(KrakSatAPITestCase):
    """Tests for /status API endpoint"""

    list_url = reverse('status-list')
    model = Status
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'phase': 'launch', 'mission_time': 5.37, 'cansat_online': True
    }

    def test_create(self):
        """Ensure we can create a new Status object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /status returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('State outside choices', {'phase': 'foobar'}),
            ('State too long', {'phase': 'foobarfoobarfoobarfoobarfoobar'}),
            ('Invalid state', {'phase': 5}),
            ('Invalid mission time', {'mission_time': 'foobar'}),
            ('Invalid cansat_online', {'cansat_online': 'foobar'}),
        )
