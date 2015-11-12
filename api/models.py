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
