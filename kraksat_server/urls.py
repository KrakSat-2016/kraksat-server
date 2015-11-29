"""kraksat_server URL Configuration"""

from django.conf.urls import include, url
from rest_framework import routers

from api.views import SHTViewSet, IMUViewSet, GPSViewSet

router = routers.DefaultRouter()
router.register(r'sht', SHTViewSet)
router.register(r'imu', IMUViewSet)
router.register(r'gps', GPSViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
