from rest_framework import viewsets
from rest_framework.response import Response


class HelloViewSet(viewsets.ViewSet):
    """
    This is hello. Cool, isn't it?
    """

    def list(self, request):
        return Response({'Hello': 'world!'})
