from rest_framework import viewsets

from api.models import SHT
from api.serializers import SHTSerializer


class SHTViewSet(viewsets.ModelViewSet):
    """SHT (Humidity and Temperature) sensor data."""
    queryset = SHT.objects.all()
    serializer_class = SHTSerializer
