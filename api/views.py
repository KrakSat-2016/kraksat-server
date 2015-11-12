from rest_framework import viewsets
from rest_framework.response import Response

from api.models import SHT
from api.serializers import SHTSerializer


class HelloViewSet(viewsets.ViewSet):
    """
    This is hello. Cool, isn't it?
    """

    def list(self, request):
        return Response({'Hello': 'world!'})


class SHTViewSet(viewsets.ModelViewSet):
    """SHT (Humidity and Temperature) sensor data."""
    queryset = SHT.objects.all()
    serializer_class = SHTSerializer
