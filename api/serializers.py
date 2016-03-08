import os

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from api.models import SHT, IMU, GPS, Photo, GSInfo, Status, PlanetaryData


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


class IMUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IMU
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pressure'].validators = [MinValueValidator(260),
                                              MaxValueValidator(1260)]


class GPSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPS
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].validators = [MinValueValidator(-90),
                                              MaxValueValidator(90)]
        self.fields['longitude'].validators = [MinValueValidator(-180),
                                               MaxValueValidator(180)]
        self.fields['direction'].validators = [MinValueValidator(0),
                                               MaxValueValidator(360)]
        self.fields['speed_over_ground'].validators = [MinValueValidator(0)]
        self.fields['active_satellites'].validators = [MinValueValidator(0)]
        self.fields['satellites_in_view'].validators = [MinValueValidator(0)]


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
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


class GSInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GSInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].validators = [MinValueValidator(-90),
                                              MaxValueValidator(90)]
        self.fields['longitude'].validators = [MinValueValidator(-180),
                                               MaxValueValidator(180)]
        self.fields['timezone'].validators = [MinValueValidator(-24 * 60),
                                              MaxValueValidator(24 * 60)]


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class PlanetaryDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetaryData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'timestamp':
                field.validators = [MinValueValidator(0)]
        self.fields['earth_similarity_index'].validators += [
            MaxValueValidator(1)]
        self.fields['adiabatic_index'].validators = [MinValueValidator(1)]
        self.fields['refractive_index'].validators = [MinValueValidator(1)]
