"""kraksat_server URL Configuration"""

from django.conf.urls import include, url
from rest_framework import routers

from api.views import SHTViewSet

router = routers.DefaultRouter()
router.register(r'sht', SHTViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
