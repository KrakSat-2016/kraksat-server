from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from api.models import SHT


class SHTSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SHT
        fields = ('url', 'timestamp', 'humidity', 'temperature')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['humidity'].validators = [MinValueValidator(0),
                                              MaxValueValidator(100)]
        self.fields['temperature'].validators = [MinValueValidator(-40),
                                                 MaxValueValidator(125)]
