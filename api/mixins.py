from rest_framework import status
from rest_framework.response import Response


class TimestampOrderingMixin:
    """ModelViewSet mixin that sets default ordering field to timestamp"""
    ordering_fields = ('timestamp',)
    ordering = ('timestamp',)


class LatestRecordMixin:
    """Retrieves first element in list()"""
    append_suffix = False

    def list(self, request, *args, **kwargs):
        obj = self.get_queryset().order_by('-timestamp').first()
        if obj is None:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
