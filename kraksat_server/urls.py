"""kraksat_server URL Configuration"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import (
    TelemetryViewSet, KundtViewSet, GPSViewSet, PhotoViewSet, GSInfoViewSet,
    LatestGSInfoViewSet, LatestStatusViewSet, StatusViewSet,
    LatestPlanetaryDataViewSet, PlanetaryDataViewSet, LatestVideoInfoViewSet,
    VideoInfoViewSet
)

router = routers.DefaultRouter()
router.register(r'telemetry', TelemetryViewSet)
router.register(r'kundt', KundtViewSet)
router.register(r'gps', GPSViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'gsinfo/latest', LatestGSInfoViewSet,
                base_name='latest_gsinfo')
router.register(r'gsinfo', GSInfoViewSet)
router.register(r'status/latest', LatestStatusViewSet,
                base_name='latest_status')
router.register(r'status', StatusViewSet)
router.register(r'planetarydata/latest', LatestPlanetaryDataViewSet,
                base_name='latest_planetarydata')
router.register(r'planetarydata', PlanetaryDataViewSet)
router.register(r'video/latest', LatestVideoInfoViewSet,
                base_name='latest_videoinfo')
router.register(r'video', VideoInfoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
