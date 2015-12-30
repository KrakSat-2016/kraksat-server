class TimestampOrderingMixin:
    """ModelViewSet mixin that sets default ordering field to timestamp"""
    ordering_fields = ('timestamp',)
    ordering = ('timestamp',)
