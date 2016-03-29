import os

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from rest_framework.permissions import SAFE_METHODS

from api.models import (
    Telemetry, GPS, Photo, GSInfo, Status, PlanetaryData, Kundt, VideoInfo
)


class FieldSubsetModelSerializer(serializers.ModelSerializer):
    """
    ModelSerializer subclass that includes only the fields requested via
    'fields' GET parameter in the response.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context['request'].method in SAFE_METHODS:
            # Return only requested fields
            fields = self.context['request'].query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field in existing - allowed:
                    self.fields.pop(field)
        else:
            self.add_validators()

    def add_validators(self):
        """Add validators to fields. Invoked only on unsafe HTTP methods"""
        pass


class TelemetrySerializer(FieldSubsetModelSerializer,
                          serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Telemetry
        fields = '__all__'

    def add_validators(self):
        self.fields['humidity'].validators = [MinValueValidator(0),
                                              MaxValueValidator(100)]
        self.fields['temperature'].validators = [MinValueValidator(-40),
                                                 MaxValueValidator(125)]
        self.fields['pressure'].validators = [MinValueValidator(260),
                                              MaxValueValidator(1260)]


class KundtSerializer(FieldSubsetModelSerializer,
                      serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kundt
        fields = '__all__'

    def add_validators(self):
        self.fields['frequency'].validators = [MinValueValidator(0)]
        self.fields['amplitude'].validators = [MinValueValidator(0)]


class GPSSerializer(FieldSubsetModelSerializer,
                    serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPS
        fields = '__all__'

    def add_validators(self):
        self.fields['latitude'].validators = [MinValueValidator(-90),
                                              MaxValueValidator(90)]
        self.fields['longitude'].validators = [MinValueValidator(-180),
                                               MaxValueValidator(180)]
        self.fields['direction'].validators = [MinValueValidator(0),
                                               MaxValueValidator(360)]
        self.fields['speed_over_ground'].validators = [MinValueValidator(0)]
        self.fields['active_satellites'].validators = [MinValueValidator(0)]
        # self.fields['satellites_in_view'].validators = [MinValueValidator(0)]


class PhotoSerializer(FieldSubsetModelSerializer,
                      serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

    def validate_image(self, value):
        name, ext = os.path.splitext(value.name)
        ext = ext[1:].upper()
        allowed_exts = settings.ALLOWED_IMAGE_EXTENSIONS
        if ext not in allowed_exts:
            raise serializers.ValidationError(
                '\'{}\': \'{}\' extension not in the list: {}'
                .format(value.name, ext, allowed_exts))

        return value


class GSInfoSerializer(FieldSubsetModelSerializer,
                       serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GSInfo
        fields = '__all__'

    def add_validators(self):
        self.fields['latitude'].validators = [MinValueValidator(-90),
                                              MaxValueValidator(90)]
        self.fields['longitude'].validators = [MinValueValidator(-180),
                                               MaxValueValidator(180)]
        self.fields['timezone'].validators = [MinValueValidator(-24 * 60),
                                              MaxValueValidator(24 * 60)]


class StatusSerializer(FieldSubsetModelSerializer,
                       serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class PlanetaryDataSerializer(FieldSubsetModelSerializer,
                              serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetaryData
        fields = '__all__'

    def add_validators(self):
        for name, field in self.fields.items():
            if name != 'timestamp':
                field.validators = [MinValueValidator(0)]
        self.fields['earth_similarity_index'].validators += [
            MaxValueValidator(1)]
        self.fields['adiabatic_index'].validators = [MinValueValidator(1)]
        self.fields['refractive_index'].validators = [MinValueValidator(1)]


class VideoInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoInfo
        fields = '__all__'
