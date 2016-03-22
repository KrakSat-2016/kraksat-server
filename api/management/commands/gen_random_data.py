import math
import random
from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from api.models import Telemetry


class Command(BaseCommand):
    help = 'Generates random SHT and IMU data'
    output_transaction = True

    def add_arguments(self, parser):
        parser.add_argument('--height', type=float, default=3000,
                            help='Starting height in meters (default: 3000)')
        parser.add_argument('--tick', type=float, default=0.5,
                            help='Time difference between two data in s '
                                 '(default: 0.5)')
        parser.add_argument('--speed', type=float, default=10,
                            help='Descent speed in m/s (default: 10)')
        parser.add_argument('--clear', action='store_true', default=False,
                            help='Clear DB before inserting new data')
        parser.add_argument('--temp-error', type=float, default=0.01,
                            help='Temperature ±error value (default: 0.01)')
        parser.add_argument('--temp-noise', type=float, default=0.01,
                            help='Temperature %% noise (default: 0.01)')
        parser.add_argument('--grav-error', type=float,
                            default=0.0005985504150390625,
                            help='Gravity ±error value (default: '
                                 '0.0005985504150390625)')
        parser.add_argument('--grav-noise', type=float, default=0.05,
                            help='Gravity %% noise (default: 0.05)')
        parser.add_argument('--pressure-error', type=float, default=20.0,
                            help='Pressure ±error value (default: 20)')
        parser.add_argument('--pressure-noise', type=float, default=0.05,
                            help='Pressure %% noise (default: 0.05)')

    def handle(self, *args, **options):
        height = options['height']
        tick = options['tick']
        step = tick * options['speed']
        dt = timezone.now()
        delta = timedelta(seconds=tick)

        telemetry = []
        while height > 0:
            temp = gen_temperature(height, options['temp_error'],
                                   options['temp_noise']) - 273.15
            grav = gen_gravity(height, options['grav_error'],
                               options['grav_noise']) / 9.80665
            pressure = gen_pressure(height, options['pressure_error'],
                                    options['pressure_noise']) / 100

            telemetry.append(Telemetry(
                    timestamp=dt,
                    voltage=0, current=0, oxygen=0, ion_radiation=0,
                    humidity=50, temperature=temp, pressure=pressure,
                    gyro_x=0, gyro_y=0, gyro_z=0,
                    accel_x=0, accel_y=grav, accel_z=0,
                    magnet_x=0, magnet_y=0, magnet_z=0))

            dt += delta
            height -= step

        if options['clear']:
            Telemetry.objects.all().delete()
        Telemetry.objects.bulk_create(telemetry)


def error_noise(func):
    """Decorator that adds error and noise arguments to data generator function

    :param function func:
    :return: wrapped function
    :rtype: function
    """

    def gen_data(height, error=0.0, noise=0.0):
        val = func(height)
        if error:
            val += error * random.uniform(-1, 1)
        if noise:
            val += val * noise * random.uniform(-1, 1)
        return val

    return gen_data


@error_noise
def gen_gravity(height):
    return (6371008.8 / (6371008.8 + height)) ** 2 * 9.80665


@error_noise
def gen_temperature(height):
    return -6.49 * height / 1000 + 273.15 + 20


@error_noise
def gen_pressure(height):
    numerator = -((9.80665 + gen_gravity(height)) / 2) * 0.0289644 * height
    denominator = 8.31432 * ((gen_temperature(height) + 273.15 + 20) / 2)
    return 101325 * math.exp(numerator / denominator)
