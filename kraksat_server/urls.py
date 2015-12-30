"""kraksat_server URL Configuration"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import (
    SHTViewSet, IMUViewSet, GPSViewSet, PhotoViewSet, GSInfoViewSet,
    LatestGSInfoViewSet
)

router = routers.DefaultRouter()
router.register(r'sht', SHTViewSet)
router.register(r'imu', IMUViewSet)
router.register(r'gps', GPSViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'gsinfo/latest', LatestGSInfoViewSet,
                base_name='latest_gsinfo')
router.register(r'gsinfo', GSInfoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
