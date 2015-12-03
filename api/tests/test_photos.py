import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile as SUF
from django.core.urlresolvers import reverse
from django.test import override_settings

from api.models import Photo
from api.tests.utils import KrakSatAPITestCase, get_resource_path


# Use temporary MEDIA_ROOT so we can easily remove uploaded images in
# tearDownClass()
@override_settings(MEDIA_ROOT=tempfile.mkdtemp(prefix='kraksat_media'))
class PhotosTests(KrakSatAPITestCase):
    """Tests for /photos API endpoint"""

    list_url = reverse('photo-list')
    model = Photo
    valid_data = {
        'timestamp': KrakSatAPITestCase.TIMESTAMP,
        'image': open(get_resource_path('test.png'), mode='rb'),
        'is_panorama': True,
    }
    send_format = 'multipart'

    @classmethod
    def tearDownClass(cls):
        # Remove temporary upload directory
        shutil.rmtree(settings.MEDIA_ROOT)

    def test_create(self):
        """Ensure we can upload a new Photo"""
        self._test_create(exclude=('image',))

    @override_settings(ALLOWED_IMAGE_EXTENSIONS=('PNG',))
    def test_invalid_params(self):
        """Ensure sending invalid parameters to /photos returns error 400"""
        invalid_contents = SUF('test.png', b'test contents', 'image/png')
        invalid_ext = SUF('invalid.ext1337', self.valid_data['image'].read(),
                          'image/png')
        self._test_invalid_params(
            ('Invalid timestamp', {'timestamp': 'foobar'}),
            ('Invalid file contents', {'image': invalid_contents}),
            ('Invalid file extension', {'image': invalid_ext}),
            ('Invalid is_panorama', {'is_panorama': 'foobar'}),
        )
