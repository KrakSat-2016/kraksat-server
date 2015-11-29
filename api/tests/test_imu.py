from django.core.urlresolvers import reverse

from api.models import IMU
from api.tests.utils import KrakSatAPITestCase


class IMUTests(KrakSatAPITestCase):
    """Tests for /imu API endpoint"""

    list_url = reverse('imu-list')
    model = IMU
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'gyro_x': 5.5, 'gyro_y': 12.5, 'gyro_z': 3.5,
        'accel_x': 0.1, 'accel_y': 0.15, 'accel_z': 0.31,
        'magnet_x': 5.001, 'magnet_y': 2.01, 'magnet_z': 9.999,
        'pressure': 1020.5
    }

    def test_create(self):
        """Ensure we can create a new IMU object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /imu returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Invalid gyro_x', {'gyro_x': 'foobar'}),
            ('Invalid gyro_y', {'gyro_y': 'foobar'}),
            ('Invalid gyro_z', {'gyro_z': 'foobar'}),
            ('Invalid accel_x', {'accel_x': 'foobar'}),
            ('Invalid accel_y', {'accel_y': 'foobar'}),
            ('Invalid accel_z', {'accel_z': 'foobar'}),
            ('Invalid magnet_x', {'magnet_x': 'foobar'}),
            ('Invalid magnet_y', {'magnet_y': 'foobar'}),
            ('Invalid magnet_z', {'magnet_z': 'foobar'}),
            ('Invalid pressure', {'pressure': 'foobar'})
        )
