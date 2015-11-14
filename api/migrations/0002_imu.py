# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(db_index=True, unique=True)),
                ('gyro_x', models.FloatField(help_text='Angular velocity (X axis) [dps]')),
                ('gyro_y', models.FloatField(help_text='Angular velocity (Y axis) [dps]')),
                ('gyro_z', models.FloatField(help_text='Angular velocity (Z axis) [dps]')),
                ('accel_x', models.FloatField(help_text='Linear acceleration (X axis) [g]')),
                ('accel_y', models.FloatField(help_text='Linear acceleration (Y axis) [g]')),
                ('accel_z', models.FloatField(help_text='Linear acceleration (Z axis) [g]')),
                ('magnet_x', models.FloatField(help_text='Magnetic field (X axis) [gauss]')),
                ('magnet_y', models.FloatField(help_text='Magnetic field (Y axis) [gauss]')),
                ('magnet_z', models.FloatField(help_text='Magnetic field (Z axis) [gauss]')),
                ('pressure', models.FloatField(help_text='Air pressure [hPa]')),
            ],
        ),
    ]
