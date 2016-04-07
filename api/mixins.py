from rest_framework import status, viewsets
from rest_framework.response import Response


class TimestampOrderingMixin:
    """ModelViewSet mixin that sets default ordering field to timestamp"""
    ordering_fields = ('timestamp',)
    ordering = ('timestamp',)


class LatestRecordModelViewSet(viewsets.ModelViewSet):
    """Retrieves the first element in list() when set ?latest=1 by GET."""

    def list(self, request, *args, **kwargs):
        if ('latest' in request.GET and
                request.GET['latest'].lower() not in ('0', 'false') and
                request.GET['latest']):
            obj = self.get_queryset().order_by('-timestamp').first()
            if obj is None:
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)
