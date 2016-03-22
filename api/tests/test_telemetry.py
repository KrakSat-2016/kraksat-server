from django.core.urlresolvers import reverse

from api.models import Telemetry
from api.tests.utils import KrakSatAPITestCase


class TelemetryTests(KrakSatAPITestCase):
    """Tests for /telemetry API endpoint"""

    list_url = reverse('telemetry-list')
    model = Telemetry
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'voltage': 0, 'current': 0, 'oxygen': 0, 'ion_radiation': 0,
        'humidity': 20, 'temperature': 30, 'pressure': 1020.5,
        'gyro_x': 5.5, 'gyro_y': 12.5, 'gyro_z': 3.5,
        'accel_x': 0.1, 'accel_y': 0.15, 'accel_z': 0.31,
        'magnet_x': 5.001, 'magnet_y': 2.01, 'magnet_z': 9.999
    }

    def test_create(self):
        """Ensure we can create a new Telemetry object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /telemetry returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Humidity below 0', {'humidity': -5}),
            ('Humidity above 100', {'humidity': 100.04}),
            ('Temperature below -40', {'temperature': -40.01}),
            ('Temperature above 125', {'temperature': 125.01}),
            ('Invalid pressure', {'pressure': 'foobar'}),
            ('Invalid gyro_x', {'gyro_x': 'foobar'}),
            ('Invalid gyro_y', {'gyro_y': 'foobar'}),
            ('Invalid gyro_z', {'gyro_z': 'foobar'}),
            ('Invalid accel_x', {'accel_x': 'foobar'}),
            ('Invalid accel_y', {'accel_y': 'foobar'}),
            ('Invalid accel_z', {'accel_z': 'foobar'}),
            ('Invalid magnet_x', {'magnet_x': 'foobar'}),
            ('Invalid magnet_y', {'magnet_y': 'foobar'}),
            ('Invalid magnet_z', {'magnet_z': 'foobar'})
        )
