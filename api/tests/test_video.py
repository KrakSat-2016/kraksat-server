from django.core.urlresolvers import reverse

from api.models import VideoInfo
from api.tests.utils import KrakSatAPITestCase


class VideoTests(KrakSatAPITestCase):
    """Tests for /video API endpoint"""

    list_url = reverse('videoinfo-list')
    model = VideoInfo
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP, 'yt_video_id': 'PaYpIdRN7cQ'
    }

    def test_create(self):
        """Ensure we can create a new VideoInfo object"""
        self._test_create()

    def test_invalid_params(self):
        """Ensure sending invalid parameters to /video returns error 400"""
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Empty video ID', {'yt_video_id': ''}),
        )
