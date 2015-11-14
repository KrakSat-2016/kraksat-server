"""kraksat_server URL Configuration"""

from django.conf.urls import include, url
from rest_framework import routers

from api.views import SHTViewSet, IMUViewSet

router = routers.DefaultRouter()
router.register(r'sht', SHTViewSet)
router.register(r'imu', IMUViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
