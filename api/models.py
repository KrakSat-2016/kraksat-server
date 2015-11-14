from django.db import models


class SHT(models.Model):
    """SHT (Humidity and Temperature) data.

    For Sensirion SHT21 sensor.
    """
    timestamp = models.DateTimeField(primary_key=True)

    humidity = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text='0 to 100%, resolution 0.04%')

    temperature = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text='-40 to 125℃, resolution 0.01℃')


class IMU(models.Model):
    """IMU (Inertial Measurement Unit) data

    For Pololu AltIMU-10
    """
    timestamp = models.DateTimeField(db_index=True, unique=True)

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
