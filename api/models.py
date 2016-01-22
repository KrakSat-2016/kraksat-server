from django.db import models


class TimestampModel(models.Model):
    """Abstract model class containing "timestamp" field"""
    timestamp = models.DateTimeField(db_index=True, unique=True)

    class Meta:
        abstract = True


class SHT(TimestampModel):
    """SHT (Humidity and Temperature) data

    For Sensirion SHT21 sensor
    """
    humidity = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text='0 to 100%, resolution 0.04%')

    temperature = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text='-40 to 125℃, resolution 0.01℃')


class IMU(TimestampModel):
    """IMU (Inertial Measurement Unit) data

    For Pololu AltIMU-10
    """
    gyro_x = models.FloatField(help_text='Angular velocity (X axis) [dps]')
    gyro_y = models.FloatField(help_text='Angular velocity (Y axis) [dps]')
    gyro_z = models.FloatField(help_text='Angular velocity (Z axis) [dps]')

    accel_x = models.FloatField(help_text='Linear acceleration (X axis) [g]')
    accel_y = models.FloatField(help_text='Linear acceleration (Y axis) [g]')
    accel_z = models.FloatField(help_text='Linear acceleration (Z axis) [g]')

    magnet_x = models.FloatField(help_text='Magnetic field (X axis) [gauss]')
    magnet_y = models.FloatField(help_text='Magnetic field (Y axis) [gauss]')
    magnet_z = models.FloatField(help_text='Magnetic field (Z axis) [gauss]')

    pressure = models.FloatField(help_text='Air pressure [hPa]')


class GPS(TimestampModel):
    """GPS data"""
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(help_text='[m]')

    direction = models.FloatField(
        help_text='Track Made Good (degrees relative to north) [°]')
    speed_over_ground = models.FloatField(help_text='[km/h]')

    active_satellites = models.PositiveSmallIntegerField()
    satellites_in_view = models.PositiveSmallIntegerField()

    # Quality
    QUALITY_NO_FIX = 'no_fix'
    QUALITY_GPS = 'gps'
    QUALITY_DGPS = 'dgps'
    QUALITY_CHOICES = (
        (QUALITY_NO_FIX, 'No Fix'),
        (QUALITY_GPS, 'GPS'),
        (QUALITY_DGPS, 'DGPS')
    )
    quality = models.CharField(max_length=6, choices=QUALITY_CHOICES)

    # Dilution Of Precision
    FIX_TYPE_NO_FIX = 'no_fix'
    FIX_TYPE_2D = '2d'
    FIX_TYPE_3D = '3d'
    FIX_TYPE_CHOICES = (
        (FIX_TYPE_NO_FIX, 'No fix'),
        (FIX_TYPE_2D, '2D'),
        (FIX_TYPE_3D, '3D')
    )
    fix_type = models.CharField(max_length=6, choices=FIX_TYPE_CHOICES)
    pdop = models.FloatField(verbose_name='PDOP',
                             help_text='Position (3D) Dilution Of Precision')
    hdop = models.FloatField(verbose_name='HDOP',
                             help_text='Horizontal Dilution Of Precision')
    vdop = models.FloatField(verbose_name='VDOP',
                             help_text='Vertical Dilution Of Precision')


class Photo(TimestampModel):
    """Photo taken during the flight"""
    image = models.ImageField()
    is_panorama = models.BooleanField()


class GSInfo(TimestampModel):
    """Information about the Ground Station"""
    latitude = models.FloatField()
    longitude = models.FloatField()
    timezone = models.IntegerField(help_text='Timezone as UTC offset in '
                                             'minutes (so e.g. UTC-01:45 '
                                             'becomes -105)')


class Status(TimestampModel):
    """Mission Status"""
    PHASE_LAUNCH_PREPARATION = 'launch_preparation'
    PHASE_COUNTDOWN = 'countdown'
    PHASE_LAUNCH = 'launch'
    PHASE_DESCENT = 'descent'
    PHASE_GROUND_OPERATIONS = 'ground_operations'
    PHASE_MISSION_COMPLETE = 'mission_complete'
    PHASE_CHOICES = (
        (PHASE_LAUNCH_PREPARATION, 'Launch preparation'),
        (PHASE_COUNTDOWN, 'Countdown'),
        (PHASE_LAUNCH, 'Launch'),
        (PHASE_DESCENT, 'Descent'),
        (PHASE_GROUND_OPERATIONS, 'Ground operations'),
        (PHASE_MISSION_COMPLETE, 'Mission complete')
    )

    phase = models.CharField(max_length=18, choices=PHASE_CHOICES, blank=True)
    mission_time = models.FloatField(
            help_text='Current mission time in seconds. Negative value means '
                      'countdown to start', null=True)
    cansat_online = models.BooleanField()
