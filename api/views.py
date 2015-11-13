import rest_framework
from rest_framework import viewsets

from api.models import SHT
from api.serializers import SHTSerializer


def get_view_name(view_cls, suffix=None):
    """Return the view name to be shown to a user.

    The function allows to specify display_name attribute for a view to be
    displayed as view name in OPTIONS responses and browsable API.
    """
    if hasattr(view_cls, 'display_name'):
        name = view_cls.display_name
        if suffix:
            name += ' ' + suffix
        return name
    if view_cls.__name__ == 'APIRoot':
        return 'API Root'

    return rest_framework.views.get_view_name(view_cls, suffix)


class SHTViewSet(viewsets.ModelViewSet):
    """SHT (Humidity and Temperature) sensor data."""
    display_name = 'SHT Data'
    queryset = SHT.objects.all()
    serializer_class = SHTSerializer
